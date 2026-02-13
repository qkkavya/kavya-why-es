import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
public class Order implements Comparable<Order>{
    private Map<Item,Integer> items;
    private int status=0; //0 denotes preparing, 1 delivered/refunded, 2 out for delivery, 3 cancelled
    private String request;
    private final String id;
    private int priority;
    public void setVIP(){
        this.priority=2;
    }
    public Order(String id){
        items=new HashMap<>();
        this.id=id;
        request="no request";
        priority=1;
    }
    public int getStatus(){
        return status;
    }
    public Set<Item> getItems(){
        return items.keySet();
    }
    public List<String> getNames(){
        List<String> m=new java.util.ArrayList<>(List.of());
        for (Item i:getItems()){
            m.add(i.getName());
        }
        return m;
    }
    public String printStatus(){
        if (status==0) return "status: preparing\n";
        else if (status==1) return "status: order cleared\n";
        else if (status==2) return "status: out for delivery\n";
        else if (status==3) return "status: order cancelled\n";
        return "\n";
    }
    public int getTotal(){
        int c=0;
        for (Item item:items.keySet()){
            c=c+(item.getPrice()*item.getQty());
        }
        return c;
    }
    public void setStatus(int status){
        this.status=status;
    }
    public String getRequest(){
        if (items.isEmpty()){
            return "no special req";
        }
        return request;
    }
    public void setRequest(String request){
        this.request=request;
    }
    public void addtoCart(String h){
        for (Map.Entry<Integer, Item> i:Admin.menu.entrySet()){
            if (i.getValue().getName().equals(h) && i.getValue().isAvailability()){
                items.put(i.getValue(),1);
                i.getValue().setPopularity(i.getValue().getPopularity()+1);
                i.getValue().setQty(1);
            }
        }
    }
    public void dropfromCart(String name){
        for (Item i:items.keySet()){
            if (i.getName().equals(name)){
                items.remove(name);
                i.setPopularity(i.getPopularity()-1);
                i.setQty(1);
            }
        }
    }
    public void clearCart(){
        items.clear();
    }
    public String getClient(){
        return id;
    }
    public int compareTo(Order o){
        return Integer.compare(o.priority, this.priority);
    }
    public String getAll() {
        if (items.keySet().isEmpty()){
            return "No items.";
        }
        StringBuilder l=new StringBuilder();
        for (Item i:items.keySet()){
            l.append(i.getName()).append(", price: ").append(i.getPrice()).append("\n");
        }
        l.append("total: ").append(getTotal()).append("\n");
        return l.toString();
    }
}