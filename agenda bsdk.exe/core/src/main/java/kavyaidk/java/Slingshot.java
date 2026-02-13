package kavyaidk.java;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;

import java.util.List;

public class Slingshot {
    private List<Bird> birdQueue;
    private Bird currentBird;
    private double launchAngle;
    private double launchForce;
    private double birdSpeed;
    private double distance;
    SpriteBatch batch;
    Texture colour;
    public Slingshot(SpriteBatch batch){
        this.batch=batch;
        colour=new Texture("slingshot.png");
    }
    public void render(int x, int y,int w,int h){
        //batch.begin();
        batch.draw(colour, x,y,w,h);
        //batch.end();
    }
    public void launchBird() throws BirdException {

    }

    public void calculateTrajectory(){

    }

    public List<Bird> getBirdQueue() {
        return birdQueue;
    }

    public void setBirdQueue(List<Bird> birdQueue) {
        this.birdQueue = birdQueue;
    }

    public Bird getCurrentBird() {
        return currentBird;
    }

    public void setCurrentBird(Bird currentBird) {
        this.currentBird = currentBird;
    }

    public double getLaunchAngle() {
        return launchAngle;
    }

    public void setLaunchAngle(double launchAngle) {
        this.launchAngle = launchAngle;
    }

    public double getLaunchForce() {
        return launchForce;
    }

    public void setLaunchForce(double launchForce) {
        this.launchForce = launchForce;
    }

    public double getBirdSpeed() {
        return birdSpeed;
    }

    public void setBirdSpeed(double birdSpeed) {
        this.birdSpeed = birdSpeed;
    }

    public double getDistance() {
        return distance;
    }

    public void setDistance(double distance) {
        this.distance = distance;
    }
}
