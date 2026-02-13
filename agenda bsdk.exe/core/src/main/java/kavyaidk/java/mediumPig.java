package kavyaidk.java;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;

public class mediumPig extends Pig{
    public mediumPig(SpriteBatch batch){
        super(batch);
        sizeMedium=new Texture("medpig.png");
    }
    public void manageHealth() throws PigException{

    }
}
