package kavyaidk.java;
import com.badlogic.gdx.ApplicationAdapter;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.Input;
import com.badlogic.gdx.audio.Music;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.OrthographicCamera;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.Batch;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.utils.ScreenUtils;
import com.badlogic.gdx.utils.viewport.FitViewport;
import com.badlogic.gdx.math.Vector3;

public class Main extends ApplicationAdapter {

    SpriteBatch batch;
    Texture image, quit, levels, bg, back, pause, settings, credits, play, menu, parade, fly,winScreen;
    Texture leveln, level1, level2, level3;
    Music music;
    OrthographicCamera camera= new OrthographicCamera();;
    RedBird red, red1,red2;
    YellowBird yellow;
    WhiteBird white;
    Slingshot sling;
    smallPig small;
    mediumPig medium;
    largePig large;
    Wood woodenBlock;
    FitViewport viewport;
    Texture r,y,w;

    boolean isLevel1Unlocked = true;
    boolean isLevel2Unlocked = false;
    boolean isLevel3Unlocked = false;
    public void create(){
        batch = new SpriteBatch();
        r=new Texture("red.png");
        y=new Texture("bi.png");
        w=new Texture("white.png");
        red = new RedBird(r);
        red1 = new RedBird(r);
        red2=new RedBird(r);
        yellow = new YellowBird(y);
        white = new WhiteBird(w);
        sling = new Slingshot(batch);
        small=new smallPig(batch);
        woodenBlock=new Wood(batch);
        winScreen=new Texture("winScreen.png");
        image = new Texture("libgdx.png");
        quit = new Texture("quit.png");
        pause = new Texture("pause.png");
        back = new Texture("home.png");
        play = new Texture("play.png");
        menu = new Texture("menu.png");
        parade = new Texture("parade.png");
        fly = new Texture("fly.png");
        levels = new Texture("levels.png");
        leveln = new Texture("4.png");
        level1 = new Texture("1.png");
        level2 = new Texture("2.png");
        level3 = new Texture("3.png");
        bg = new Texture("bg.png");
        settings = new Texture("settings.png");
        credits = new Texture("credits.png");
        music = Gdx.audio.newMusic(Gdx.files.internal("abc.mp3"));
        music.setLooping(true);
        music.setVolume(.5f);
        music.play();
        viewport=new FitViewport(70,50);
    }

    public void resize(int width,int height){
        viewport.update(width,height,true);
    }

    public void render(){
        ScreenUtils.clear(Color.BLACK);
        viewport.apply();
        batch.setProjectionMatrix(viewport.getCamera().combined);
        int m=input();
        batch.begin();
        if (m==0){
            batch.draw(image, 0, 0, viewport.getWorldWidth(), viewport.getWorldHeight());
            batch.draw(menu, 17, 25, 10, 5);
            batch.draw(play, 28, 25, 10, 5);
            batch.draw(parade, 39, 25, 10, 5);
        }
        if (m==1){
            batch.draw(levels, 0, 0, viewport.getWorldWidth(), viewport.getWorldHeight());
            batch.draw(level1, 20, 20, 5, 5);
            batch.draw(leveln, 30, 20, 5, 5);
            batch.draw(leveln, 40, 20, 5, 5);
            batch.draw(back, 30, 10, 5, 5);
            if (isLevel2Unlocked) {
                batch.draw(level2, 30, 20, 5, 5);
            }
            if (isLevel3Unlocked) {
                batch.draw(level3, 40, 20, 5, 5);
            }
        }
        if (m==2){
            batch.draw(fly, 0, 0, viewport.getWorldWidth(), viewport.getWorldHeight());
            batch.draw(back, 1, viewport.getWorldHeight()-6,5,5);
        }
        if (m==3){
            batch.draw(settings, 0, 0, viewport.getWorldWidth(), viewport.getWorldHeight());
            batch.draw(back, 1, viewport.getWorldHeight()-6,5,5);
        }
        if (m==4){ //level 1 screen
            batch.draw(bg, 0, 0, viewport.getWorldWidth(), viewport.getWorldHeight());
            red.draw(batch);
            red.sprite.setPosition(1,7);
            red1.draw(batch);
            red2.draw(batch);
            red2.sprite.setPosition(6,7);
            red1.sprite.setPosition(9,12);
            red1.enableDragAndDrop(viewport.getCamera());
            red.update(Gdx.graphics.getDeltaTime());
            sling.render(8, 6, 10, 10);
            small.render(60,17,4,5);
            woodenBlock.render(60,12,5,5);
            woodenBlock.render(60,7,5,5);
            batch.draw(pause, 1, viewport.getWorldHeight() - 6, 5, 5);
        }
        if (m==5){ //level 2 screen
            batch.draw(bg, 0, 0, viewport.getWorldWidth(), viewport.getWorldHeight());
            yellow.draw(batch);
            red.draw(batch);
            red.sprite.setPosition(1,7);
            yellow.sprite.setPosition(6,7);
            yellow.enableDragAndDrop(viewport.getCamera());
            sling.render(8, 6, 8, 8);
            batch.draw(pause, 1, viewport.getWorldHeight() - 6, 5, 5);
        }
        if (m==6){//level 3 screen
            batch.draw(bg, 0, 0, viewport.getWorldWidth(), viewport.getWorldHeight());
            red.draw(batch);
            yellow.draw(batch);
            white.draw(batch);
            red.sprite.setPosition(1,7);
            yellow.sprite.setPosition(6,7);
            white.sprite.setPosition(11,7);
            white.enableDragAndDrop(viewport.getCamera());
            sling.render(13, 6, 8, 8);
            batch.draw(pause, 1, viewport.getWorldHeight() - 6, 5, 5);
        }
        if (m==7 || m==8 || m==9){
            batch.draw(quit, 0, 0, viewport.getWorldWidth(), viewport.getWorldHeight());
        }
        if (m==10){
            batch.draw(credits, 0, 0, viewport.getWorldWidth(), viewport.getWorldHeight());
            batch.draw(back, 1, viewport.getWorldHeight()-4,3,3);
        }
        if(m==11){ //winning screen
            batch.draw(winScreen,0, 0, viewport.getWorldWidth(), viewport.getWorldHeight());
        }
        batch.end();
    }
    int k=0;
    private int input(){
        Vector3 worldCoordinates = viewport.unproject(new Vector3(Gdx.input.getX(), Gdx.input.getY(), 0));
        float mouseX=worldCoordinates.x;
        float mouseY=worldCoordinates.y;

        if (Gdx.input.isButtonPressed(Input.Buttons.LEFT) && k==0){ // home screen
            if (mouseX>=28 && mouseX<=38 && mouseY>=25 && mouseY<=30){
                k=1;
                return k;
            }
            if (mouseX>=39 && mouseX<=49 && mouseY>=25 && mouseY<=30){
                k=2;
                return k;
            }
            if (mouseX>=17 && mouseX<=27 && mouseY>=25 && mouseY<=30){
                k=3;
                return k;
            }
        }
        if (Gdx.input.isButtonPressed(Input.Buttons.LEFT) && k==1){ // levels screen
            if (Gdx.input.isButtonPressed(Input.Buttons.LEFT)){
                if (mouseX>=30 && mouseX<=35 && mouseY>=10 && mouseY<=15){
                    k=0;
                    return k;
                }
                if(mouseX>=20 && mouseX<=25 && mouseY>=20 && mouseY<=25 && isLevel1Unlocked){
                    k=4;
                    return k;
                }
                if(mouseX>=30 && mouseX<=35 && mouseY>=20 && mouseY<=25 && isLevel2Unlocked){
                    k=5;
                    return k;
                }
                if(mouseX>=40 && mouseX<=45 && mouseY>=20 && mouseY<=25 && isLevel3Unlocked){
                    k=6;
                    return k;
                }
            }
        }
        if (Gdx.input.isButtonPressed(Input.Buttons.LEFT) && k==3){ // menu options
            if (mouseX>=15 && mouseX<=42 && mouseY>=25 && mouseY<=30){
                music.setVolume(.5f);
            }
            if (mouseX>=15 && mouseX<=32 && mouseY>=20 && mouseY<=25){
                music.setVolume(0f);
            }
            if (mouseX>=15 && mouseX<=40 && mouseY>=13 && mouseY<=18){
                k=10;
                return k;
            }
        }
        if(k==4 && Gdx.input.isKeyPressed(Input.Keys.ENTER)){
            //enter will be replaced with level completion logic later
            isLevel2Unlocked = true;
            k = 1; //1 to 11
        }
        if(k==5 && Gdx.input.isKeyPressed(Input.Keys.ENTER)){
            //enter will be replaced with level completion logic later
            isLevel3Unlocked=true;
            k=1;
        }
        if(k==6 && Gdx.input.isKeyPressed(Input.Keys.ENTER)){
            //enter will be replaced with level completion logic later
            k=1;
        }
        if (Gdx.input.isButtonPressed(Input.Buttons.LEFT) && (k==3)){ //home button
            if (mouseX>=1 && mouseX<=6 && mouseY>= viewport.getWorldHeight()-6 && mouseY<= viewport.getWorldHeight()-1){
                k=0;
                return k;
            }
        }
        if(Gdx.input.isButtonPressed(Input.Buttons.LEFT) && (k==2||k==10)){
            if(mouseX>=1 && mouseX<=6 && mouseY>= viewport.getWorldHeight()-6 && mouseY<= viewport.getWorldHeight()-1){
                k=0;
                return k;
            }
        }

        if(Gdx.input.isButtonPressed(Input.Buttons.LEFT) && (k==4||k==5||k==6)){
            if(mouseX>=1 && mouseX<=6 && mouseY>= viewport.getWorldHeight()-6 && mouseY<= viewport.getWorldHeight()-1){
                k=k+3;
                return k;
            }
        }
        if(Gdx.input.isButtonPressed(Input.Buttons.LEFT) && (k==7||k==8||k==9)){
            if (mouseY>=20 && mouseY<=25){
                if (mouseX>=10 && mouseX<=30){
                    k=k-3;
                }
                if (mouseX>=35 && mouseX<=50){
                    k=0;
                }
            }
        }
        return k;
    }
    public void dispose() {
        batch.dispose();
        image.dispose();
    }
}