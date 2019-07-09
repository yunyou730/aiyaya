require "gameconfig"
require "ActorFactory"

function love.load()
    local a1 = ActorFactor:create(50,30);
    a1:setCollisionColor(1,0,0);
    a1:setPos(50,100);
    local a2 = ActorFactor:create(100,30);
    a2:setCollisionColor(1,1,0);
    a2:setPos(80,200);
    local a3 = ActorFactor:create(60,50);
    a3:setCollisionColor(0,1,1);
    a3:setPos(100,250);
end

function love.draw()
	love.graphics.print("aiyaya730",GameCfg.width,GameCfg.height);
    for uuid,actor in pairs(ActorFactor:getActorHash()) do
       actor:draw();
    end
end
