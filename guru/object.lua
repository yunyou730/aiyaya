
Object = {};

Object.objCount = 0;

function Object:create()
	Object.objCount = Object.objCount + 1;
	local instance = {};
	setmetatable(instance,self.prototype)
	return instance;
end

-- static func
function Object:outputObjectTag(object)
	print(object.tag);
end

-- members
Object.prototype = {};
Object.prototype.__index = Object.prototype;

Object.prototype.__gc = function(instance)
	print(instance,"destroye");
end

Object.prototype.tag = 999;
Object.prototype.abc = 123;

function Object.prototype:toString()
	return tostring(self);
end


