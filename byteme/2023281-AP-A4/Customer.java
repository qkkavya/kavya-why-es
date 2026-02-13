import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.util.ArrayList;
import java.util.Scanner;
public class Customer{
    private Order cart;
    private int balance;
    private ArrayList<Order> history;
    private String address;
    //File hi;
    public String getPassword(){
        return password;
    }
    public String getAddress(){
        return address;
    }
    private String ID;
    public String getID() {
        return ID;
    }
    private String password;
    public Customer(int k, String f){
        this.cart=new Order(f+1);
        this.balance=k;
        this.address="IIITD Girls Hostel";
        //this.hi=new File(String.valueOf(Path.of("history.txt")));
        this.history=new ArrayList<>();
    }
    public void signup(String id){
        Scanner scanner=new Scanner(System.in);
        System.out.print("enter password:");
        this.ID=id;
        this.password=scanner.nextLine();
    }
    public boolean login(String id, String pwd){
        if (pwd.equals(this.password) && id.equals(this.ID)){
            System.out.println("login successful!");
            return true;
        }
        else{
            System.out.println("incorrect password");
            return false;
        }
    }
    public Order getCart(){
        return cart;
    }
    public void setVip(){
        cart.setVIP();
        balance=balance-500;
    }
    public void getHistory() throws IOException{
        //return Files.readString(Path.of("history.txt"));
        if (history.isEmpty()){
            System.out.println("no pending orders.");
        }
        else{
            int index=1;
            for (Order order:history){
                System.out.println(index+". "+order.getClient());
                if (order.getRequest()!=null) System.out.println(order.getRequest());
                index++;
            }
        }
    }
    public void checkout() throws IOException{
        if (balance<cart.getTotal()){
            System.out.println("not enough money");
            return;
        }
        balance=balance-cart.getTotal();
        Admin.all.add(cart);
        history.add(cart);
        //Files.write(Paths.get("history.txt"),cart.getNames(), StandardOpenOption.APPEND);
        this.cart=new Order(ID+(history.size()+1));
    }
    public void refund(){
        if (cart.getStatus()==3){
            balance=balance+cart.getTotal();
            cart.setStatus(1);
        }
    }
    public String getBalance(){
        return String.valueOf(balance);
    }
}