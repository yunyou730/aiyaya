require "actor"

ActorFactor = {};
ActorFactor.uuidCounter = 0;
ActorFactor.hash = {};

function ActorFactor:create(width,height)
    self.uuidCounter = self.uuidCounter + 1;
    local uuid = self.uuidCounter;
    local actor = Actor:create(uuid);
    actor:setCollision(width,height);
    self.hash[uuid] = actor;
    return actor;
end

function ActorFactor:dispose(uuid)
    local actor = self.hash[uuid];
    actor:dispose();
    self.hash[uuid] = nil;
end

function ActorFactor:getActorByUUID(uuid)
    return self.hash[uuid] or nil;
end

function ActorFactor:getActorHash()
    return self.hash;
end

