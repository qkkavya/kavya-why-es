package kavyaidk.java;
import java.io.IOException;
import java.util.List;

public class Game {
    private Level currentLevel;
    private int score;
    private int remainingBirds;
    private List<Pig> pigStatus;
    private List<Block> blockStatus;

    public void saveGame() throws GameException, IOException {

    }

    public void loadGame() throws GameException,ClassNotFoundException,IOException{

    }

    public void restartGame() throws UnableToRestartGameException{

    }

    public void continueGame() throws UnableToContinueGameException{

    }

    public Level getCurrentLevel() {
        return currentLevel;
    }

    public void setCurrentLevel(Level currentLevel) {
        this.currentLevel = currentLevel;
    }

    public int getScore() {
        return score;
    }

    public void setScore(int score) {
        this.score = score;
    }

    public int getRemainingBirds() {
        return remainingBirds;
    }

    public void setRemainingBirds(int remainingBirds) {
        this.remainingBirds = remainingBirds;
    }

    public List<Pig> getPigStatus() {
        return pigStatus;
    }

    public void setPigStatus(List<Pig> pigStatus) {
        this.pigStatus = pigStatus;
    }

    public List<Block> getBlockStatus() {
        return blockStatus;
    }

    public void setBlockStatus(List<Block> blockStatus) {
        this.blockStatus = blockStatus;
    }
}