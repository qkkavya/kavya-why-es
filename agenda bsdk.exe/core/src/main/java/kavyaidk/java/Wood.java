package kavyaidk.java;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;

public class Wood extends Block{
    public Wood(SpriteBatch batch){
        super(batch);
        woodenBlock=new Texture("block.png");
    }

    public void checkDurability() throws BlockException{

    }

}
