package kavyaidk.java;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.InputAdapter;
import com.badlogic.gdx.graphics.Camera;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.Batch;
import com.badlogic.gdx.graphics.g2d.Sprite;
import com.badlogic.gdx.math.Vector;
import com.badlogic.gdx.math.Vector2;
import com.badlogic.gdx.math.Vector3;

public abstract class Bird extends InputAdapter {
    public Sprite sprite;
    private Vector2 position;
    private Vector2 velocity;
    private boolean isLaunched;
    private Vector2 initialTouchPos;
    private boolean isTouchingBird;
    private float launchStrength;
    private final float slingshotRadius=5f;
    private Vector2 slingshotAnchor;

    public Bird(Texture x) {
        this.sprite = new Sprite(x);
        sprite.setSize(4, 5);
        this.position = new Vector2(9, 12);
        this.velocity = new Vector2(0, 0);
        this.isLaunched = false;
        this.isTouchingBird = false;
        this.launchStrength = 1f;
        sprite.setPosition(position.x, position.y);
    }
    public void update(float deltaTime) {
        if (isLaunched){
            float g = -9.8f;
            velocity.y += g * deltaTime;
            position.add(velocity.x * deltaTime, velocity.y * deltaTime);
            sprite.setPosition(position.x, position.y);
        }
    }
    public void launch(Vector2 velocity){
        this.velocity.set(velocity);
        this.isLaunched = true;
    }
    public void draw(Batch batch) {
        sprite.draw(batch);
    }

    public void drawTrajectory(Batch batch){
        if(!isLaunched && isTouchingBird){
            Vector2 dragOffset=slingshotAnchor.cpy().sub(position);
            float strength=dragOffset.len();
            Vector2 velocity=dragOffset.nor().scl(strength*2);

            float g=-9.8f;
            float timeStep=0.1f;
            Vector2 tempPos=new Vector2(position);
            for(int i=0;i<30;i++){
                tempPos.x+=velocity.x*timeStep;
                tempPos.y+=velocity.y*timeStep;
                velocity.y+=g*timeStep;
            }
        }
    }

    public void enableDragAndDrop(Camera camera) {
        Gdx.input.setInputProcessor(new InputAdapter() {
            @Override
            public boolean touchDown(int screenX, int screenY, int pointer, int button) {
                Vector3 touchPos = new Vector3(screenX, screenY, 0);
                camera.unproject(touchPos);
                if (sprite.getBoundingRectangle().contains(touchPos.x, touchPos.y)) {
                    isTouchingBird = true;
                    initialTouchPos = new Vector2(touchPos.x, touchPos.y);
                }

                return true;
            }
            @Override
            public boolean touchDragged(int screenX, int screenY, int pointer) {
                if (isTouchingBird) {
                    Vector3 touchPos = new Vector3(screenX, screenY, 0);
                    camera.unproject(touchPos);
                    position.set(touchPos.x, touchPos.y); // Update bird's position based on touch
                    sprite.setPosition(position.x, position.y);
                }
                return false;
            }
            @Override
            public boolean touchUp(int screenX, int screenY, int pointer, int button) {
                sprite.translateX(2f);
                if (!isTouchingBird && position!=initialTouchPos){
                    Vector2 launchVelocity=new Vector2(2f, 0f);
                    launch(launchVelocity);
                }
                return true;
            }
        });
    }
}
