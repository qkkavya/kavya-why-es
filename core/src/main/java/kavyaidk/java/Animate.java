package kavyaidk.java;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.InputAdapter;
import com.badlogic.gdx.graphics.Camera;
import com.badlogic.gdx.math.Vector3;
import com.badlogic.gdx.physics.box2d.Body;

public class Animate {
//    private Body body;
//    private boolean isDragging=false;
//    private float offsetX, offsetY;
//    public void enableDragAndDrop(Camera camera){
//        Gdx.input.setInputProcessor(new InputAdapter(){
//            @Override
//            public boolean touchDown(int screenX, int screenY, int pointer, int button) {
//                Vector3 touchPos = new Vector3(screenX, screenY, 0);
//                camera.unproject(touchPos);
//                if (sprite.getBoundingRectangle().contains(touchPos.x, touchPos.y)) {
//                    isDragging = true;
//                    offsetX = touchPos.x - sprite.getX();
//                    offsetY = touchPos.y - sprite.getY();
//                }
//                return true;
//            }
//            @Override
//            public boolean touchDragged(int screenX, int screenY, int pointer){
//                if (isDragging) {
//                    Vector3 touchPos = new Vector3(screenX, screenY, 0);
//                    camera.unproject(touchPos);
//                    sprite.setPosition(touchPos.x - offsetX, touchPos.y - offsetY);
//                }
//                return true;
//            }
//            @Override
//            public boolean touchUp(int screenX, int screenY, int pointer, int button) {
//                isDragging = false;
//                return true;
//            }
//        });
//    }
}
