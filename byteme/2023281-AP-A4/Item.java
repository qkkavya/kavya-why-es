import java.util.ArrayList;
public class Item{
    private final String name;
    private int price;
    private String category;
    private boolean availability;
    private int popularity;
    private int qty;
    public void setQty(int qty){
        this.qty=qty;
    }
    ArrayList<String> reviews=new ArrayList<>();
    public Item(String name, int price, String category){
        this.name=name;
        this.price = price;
        this.category = category;
        this.availability=true;
        this.popularity=0;
        this.qty=1;
    }
    public int getPrice(){
        return price;
    }
    public void setPrice(int price){
        this.price=price;
    }
    public String getName(){
        return name;
    }
    public String getCategory(){
        return category;
    }
    public void setCategory(String category){
        this.category=category;
    }
    public boolean isAvailability(){
        return availability;
    }
    public void setAvailability(boolean availability){
        this.availability=availability;
    }
    public int getPopularity(){
        return popularity;
    }
    public void setPopularity(int popularity){
        this.popularity=popularity;
    }
public String viewReviews(){
    if (reviews.isEmpty()) return "no reviews found.";
    else{
        StringBuilder reviewList=new StringBuilder();
        int index=1;
        for (String review : reviews){
            reviewList.append(index).append(". ").append(review).append("\n");
            index++;
        }
        return reviewList.toString();
    }
}
    public int getQty(){
        return qty;
    }
}