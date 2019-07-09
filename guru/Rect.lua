
Actor = {};
Actor.prototype = {};
Actor.prototype.__index = Actor.prototype;

function Actor:create()
	local instance = {};
	setmetatable(instance,self.prototype);
	return instance;
end


