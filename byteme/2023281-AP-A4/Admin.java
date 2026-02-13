import java.util.*;

public class Admin{
    public static TreeMap<Integer, Item> menu=new TreeMap<>();
    public static PriorityQueue<Order> all=new PriorityQueue<>();
    private static ArrayList<Order> done=new ArrayList<>();
    public static int orders=0;
    public static int sales=0;
    public static void addItem(Item x){
        menu.put(x.getPrice(),x);
    }
    public static void removeItem(String x){
        Item j=null;
        for (Map.Entry<Integer, Item> entry:Admin.menu.entrySet()){
            if(entry.getValue().getName().equals(x)){
                menu.remove(entry.getValue().getPrice(),entry.getValue());
                j=entry.getValue();
            }
        }
        for (Order order:all){
            if (order.getItems().contains(j)) order.setStatus(3);
        }
    }
    public static void updateItem(String x,int p,String c,boolean a){
        for (Map.Entry<Integer, Item> entry:Admin.menu.entrySet()){
            if(entry.getValue().getName().equals(x)){
                menu.remove(entry.getValue().getPrice(),entry.getValue());
                entry.getValue().setPrice(p);
                entry.getValue().setCategory(c);
                entry.getValue().setAvailability(a);
            }
        }
    }
    public static void viewPending(){
        if (all.isEmpty()){
            System.out.println("no pending orders.");
        }
        else{
            int index=1;
            for (Order order:all){
                System.out.println(index+". "+order.getClient());
                if (order.getRequest()!=null) System.out.println(order.getRequest());
                index++;
            }
        }
    }
    public static void updateStatus(String id,int stat){
        for (Order order:all){
            if(order.getClient().equals(id)){
                order.setStatus(stat);
                if (stat==1){
                    all.remove(order);
                    done.add(order);
                }
            }
        }
    }
    public static void report(){
        for (Order order:done){
            System.out.println("order "+order.getClient()+" total: "+order.getTotal());
            Admin.orders++;
            Admin.sales=Admin.sales+order.getTotal();
        }
        System.out.println("Total orders: "+Admin.orders);
        System.out.println("Total sales: "+Admin.sales);
    }
    public static String printMenu(int k, String category){
        StringBuilder l=new StringBuilder();
        NavigableMap<Integer, Item> h;
        int index=1;
        if (k==6) h=menu.descendingMap();
        else h=menu;
        for (Map.Entry<Integer, Item> entry:h.entrySet()){
            if (category.equals(entry.getValue().getCategory()) || category.equals("all") || category.equals(entry.getValue().getName())){
                l.append(index).append(". ").append(entry.getValue().getName());
                l.append(", price: ").append(entry.getKey());
                l.append(", availability: ").append(entry.getValue().isAvailability()).append("\n");
                index++;
            }
        }
        return l.toString();
    }
}