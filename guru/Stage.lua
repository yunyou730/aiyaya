
Stage = {};

function Stage:create()
    local instance = {};
    setmetatable(self,self.prototype);
    return instance;
end

Stage.prototype = {};
Stage.prototype.__index = Stage.prototype;

Stage.prototype.width = 0;
Stage.prototype.height = 0;

function Stage.proto


