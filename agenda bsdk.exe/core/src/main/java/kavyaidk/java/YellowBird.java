package kavyaidk.java;

import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.Sprite;
import com.badlogic.gdx.physics.box2d.World;

public class YellowBird extends Bird{
    Texture yellow=new Texture("yellow.png");
    public YellowBird(Texture batch){
        super(batch);
    }
    public void speedBoost(){

    }

    public void launch() throws BirdException {

    }

    public void hit() throws BirdException {

    }
}