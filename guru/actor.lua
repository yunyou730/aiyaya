
Actor = {};

-- static functions
function Actor:create(uuid)
	local instance = {};
	setmetatable(instance,self.prototype);
    instance.uuid = uuid;

    -- collision
    instance.collision = {};
    instance.collision.color = { 1.0,1.0,0.5 };
    instance.collision.x = 0;      -- left down offset of collision
    instance.collision.y = 0;      
    instance.collision.width = 0;
    instance.collision.height = 0;

	return instance;
end

Actor.prototype = {};
Actor.prototype.__index = Actor.prototype;

-- members
Actor.prototype.uuid = 0;   -- uuid

-- pos
Actor.prototype.x = 0;      -- left down pos
Actor.prototype.y = 0;



-- sprite
Actor.sprite = nil;

-- member functions
function Actor.prototype:dispose()
    print("dipsose uuid:" + self.uuid);
end

function Actor.prototype:setCollision(width,height)
   self.width = width;
   self.height = height;         
end

function Actor.prototype:draw()
    self:_drawCollision();
    self:_drawSprite();
end

function Actor.prototype:_drawCollision()
    love.graphics.setColor(self.collision.color);
    local x = self.x + self.collision.x;
    local y = self.y + self.collision.y;
    love.graphics.rectangle("line",x,y,self.width,self.height);
end

function Actor.prototype:_drawSprite()
    if self.sprite == nil then
        return;
    end
end

function Actor.prototype:setCollisionColor(r,g,b)
    self.collision.color = {r,g,b};
end

function Actor.prototype:setPos(x,y)
    self.x = x;
    self.y = y;
end

function Actor.prototype:getPos()
    return {self.x,self.y};
end
