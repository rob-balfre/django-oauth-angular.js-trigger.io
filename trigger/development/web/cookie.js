// Adapted from https://github.com/bmeck/node-cookiejar/

var Cookie=exports.Cookie=function Cookie(cookiestr) {
	if(cookiestr instanceof Cookie) {
		return cookiestr;
	}
    else {
        if(this instanceof Cookie) {
        	this.name = null;
        	this.value = null;
        	this.expiration_date = Infinity;
        	this.path = "/";
        	this.domain = null;
        	this.secure = false; //how to define?
        	this.noscript = false; //httponly
        	if(cookiestr) {
        		this.parse(cookiestr)
        	}
        	return this;
        }
        return new Cookie(cookiestr)
    }
}

Cookie.prototype.toString = function toString() {
	var str=[this.name+"="+encodeURIComponent(this.value)];
	if(this.expiration_date !== Infinity) {
		str.push("expires="+(new Date(this.expiration_date)).toGMTString());
	}
	if(this.domain) {
		str.push("domain="+this.domain);
	}
	if(this.path) {
		str.push("path="+this.path);
	}
	if(this.secure) {
		str.push("secure");
	}
	if(this.noscript) {
		str.push("httponly");
	}
	return str.join("; ");
}

Cookie.prototype.toValueString = function toValueString() {
	return this.name+"="+this.value;
}

var cookie_str_splitter=/[:](?=\s*[a-zA-Z0-9_\-]+\s*[=])/g
Cookie.prototype.parse = function parse(str) {
	if(this instanceof Cookie) {
    	var parts=str.split(";")
    	, pair=parts[0].match(/([^=]+)=((?:.|\n)*)/)
    	, key=pair[1]
    	, value=pair[2];
    	this.name = key;
    	this.value = decodeURIComponent(value);
    
    	for(var i=1;i<parts.length;i++) {
    		pair=parts[i].match(/([^=]+)(?:=((?:.|\n)*))?/)
    		, key=pair[1].trim().toLowerCase()
    		, value=pair[2];
    		switch(key) {
    			case "httponly":
    				this.noscript = true;
    			break;
    			case "expires":
    				this.expiration_date = value
    					? Number(Date.parse(value))
    					: Infinity;
    			break;
    			case "path":
    				this.path = value
    					? value.trim()
    					: "";
    			break;
    			case "domain":
    				this.domain = value
    					? value.trim()
    					: "";
    			break;
    			case "secure":
    				this.secure = true;
    			break
    		}
    	}
    
    	return this;
	}
    return new Cookie().parse(str)
}

Cookie.prototype.matches = function matches(access_info) {
	if(this.noscript && access_info.script
	|| this.secure && !access_info.secure
	|| !this.collidesWith(access_info)) {
		return false
	}
	return true;
}

Cookie.prototype.collidesWith = function collidesWith(access_info) {
	if((this.path && !access_info.path) || (this.domain && !access_info.domain)) {
		return false
	}
	if(this.path && access_info.path.indexOf(this.path) !== 0) {
		return false;
	}
	if (this.domain===access_info.domain) {
		return true;
	}
	else if(this.domain && this.domain.charAt(0)===".")
	{
		var wildcard=access_info.domain.indexOf(this.domain.slice(1))
		if(wildcard===-1 || wildcard!==access_info.domain.length-this.domain.length+1) {
			return false;
		}
	}
	else if(this.domain){
		return false
	}
	return true;
}