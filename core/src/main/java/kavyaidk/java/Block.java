package kavyaidk.java;
import java.util.List;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.Sprite;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;

abstract class Block {
    SpriteBatch batch;
    private int durability;
    private int x; //x and y coordinates for position
    private int y;
    private String material;
    private List<Block> blocks;
    Texture woodenBlock;
    public Block(SpriteBatch batch){
        this.batch=batch;
    }
    public void render(int x, int y,int w,int h){
        batch.draw(woodenBlock,x,y,w,h);
    }

    Block(List<Block> blocks) {
        this.blocks = blocks;
    }

    public abstract void checkDurability() throws BlockException;

    public boolean isBroken(){
        return durability<=0;
    }

    public void addBlock(Block block){
        blocks.add(block);
    }

    public int getDurability() {
        return durability;
    }

    public void setDurability(int durability) {
        this.durability = durability;
    }

    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }

    public String getMaterial() {
        return material;
    }

    public void setMaterial(String material) {
        this.material = material;
    }

    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }

    public List<Block> getBlocks() {
        return blocks;
    }

    public void setBlocks(List<Block> blocks) {
        this.blocks = blocks;
    }
}
