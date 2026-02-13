package kavyaidk.java;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;

public class smallPig extends Pig{
    public smallPig(SpriteBatch batch){
        super(batch);
        sizeSmall=new Texture("small.png");
    }

    public void manageHealth() throws PigException{

    }
}
