package kavyaidk.java;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.Sprite;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;

abstract class Pig {
    SpriteBatch batch;
    private int health;
    private int x;
    private int y;
    Texture sizeSmall,sizeMedium,sizeLarge;
    public Pig(SpriteBatch batch){
        this.batch=batch;
    }
    public void render(int x, int y,int w,int h){
        batch.draw(sizeSmall, x,y,w,h);
        //batch.draw(sizeMedium,x,y,w,h);
    }

    public abstract void manageHealth() throws PigException;

    public boolean isDead(){
        if(health<=0){
            return true;
        }
        return false;
    }

    public int getHealth() {
        return health;
    }

    public void setHealth(int health) {
        this.health = health;
    }

    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }

    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }
}

