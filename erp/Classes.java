import java.util.Scanner;
import java.util.ArrayList;
class InvalidLoginException extends Exception{
    public InvalidLoginException(){
        super("invalid email or password.\n");
    }
}
class CourseFullException extends Exception{
    public CourseFullException(){
        super("course full.\n");
    }
}
class DropDeadlinePassedException extends Exception{
    public DropDeadlinePassedException(){
        super("deadline passed.\n");
    }
}
class Feedback<T>{
    T obj;
    public static ArrayList<Feedback> feedback=new ArrayList<>();
    private String profemail;
    Feedback(String profemail, T obj){
        this.profemail=profemail;
        this.obj=obj;
    }
    public T getFeedback(){ 
        return this.obj; 
    }
    public String getProf(){
        return profemail;
    }
}
class Course{
    private String code;
    private String name;
    private String prof="not assigned";
    private String TA="not assigned";
    private int sem;
    private String location="not assigned";
    private String timings="not assigned";
    private Course pr=null;
    public int capacity=1;//set as 1 for easier demonstration of program
    public int daysLefttoDrop=3;
    public ArrayList<String> students=new ArrayList<>();
    public Course(String code, String name, int sem){
        this.code=code;
        this.name=name;
        this.sem=sem;
    }
    public String getCourse(){
        return code+": "+name+": "+sem;
    }
    public String getCode(){
        return code;
    }
    public void setProf(String p){
        this.prof=p;
    }
    public void setTA(String p){
        this.TA=p;
    }
    public String getProf(){
        return prof;
    }
    public String getTA(){
        return TA;
    }
    public int getSem(){
        return sem;
    }
    public Course getPrerequisite(){
        return pr;
    }
    public void addStudent(String email){
        students.add(email);
    }
    public void removeStudent(String email){
        students.remove(email);
    }
    public String getLocation(){
        return location;
    }
    public String getTimings(){
        return timings;
    }
    public void setLocation(String location){
        this.location=location;
    }
    public void setTimings(String timings){
        this.timings=timings;
    }
}
class Complaint{
    private String email;
    private String description;
    private int status;
    private static ArrayList<Complaint> complaints=new ArrayList<>();
    public Complaint(String email, String description){
        this.email=email;
        this.description=description;
        this.status=0;
        complaints.add(this);
    }
    public String getID(){
        return email;
    }
    public String getDescription(){
        return description;
    }
    public int getStatus(){
        return status;
    }
    public void resolve(){
        this.status=1;
    }
    public static void viewComplaints(){
        if (complaints.isEmpty()){
            System.out.println("no complaints found.");
        } 
        else{
            int index=1;
            for (Complaint complaint:complaints){
                System.out.println(index+". "+complaint.description);
                index++;
            }
        }
    }
    public static void resolveComplaint(int index){
        if (index>0 && index<=complaints.size()){
            Complaint complaint=complaints.get(index-1);
            complaint.resolve();
            System.out.println("complaint resolved.");
        } 
        else{
            System.out.println("invalid complaint number.");
        }
    }
}