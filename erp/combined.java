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
abstract class User{
    protected String email;
    protected String password;
    public static ArrayList<Course> all=new ArrayList<>();
    public void initializeCourses(){
        all.add(new Course("CSE101", "Introduction to Programming", 1));
        all.add(new Course("MTH101", "Linear Algebra", 1));
        all.add(new Course("DES101", "Introduction to HCI", 1));
        all.add(new Course("ECE101", "Digital Circuits", 1));
        all.add(new Course("COM101", "Communication Skills", 1));
        all.add(new Course("CSE102", "Data Structures and Algorithms", 2));
        all.add(new Course("ECE201", "Computer Organization", 2));
        all.add(new Course("MTH201", "Probability and Statistics", 2));
        all.add(new Course("SSH101", "CTRSS", 2));
        all.add(new Course("SOC100", "Sociology", 2));
    }
    public User(String email){
        this.email=email;
    }
    public int signup(){
		Scanner scanner=new Scanner(System.in);
        System.out.print("enter password:");
        this.password=scanner.nextLine();
        System.out.println("signed up successfully!");
        return 1;
	}
	public int login(String id, String pwd) throws InvalidLoginException{
        if (pwd.equals(this.password) && id.equals(this.email)){
            System.out.println("login successful!");
            return 10;
        } 
        else{
            throw new InvalidLoginException();
        }
    }
}
class Prof extends User{
	public Prof(String email){
        super(email);
    }
    public void viewStudents(String code){
        for (Course course:all){
            if (course.getCode().equals(code)){
                System.out.println("students");
                for (String s:course.students){
                    System.out.println(s);
                }
            }
        }
    }
    public void viewCourses(){
        System.out.println("courses");
        for (Course course:all){
            if (course.getProf().equals(email)){
                System.out.println(course.getCourse());
            }
        }
    }
    public void viewFeedback(){
        System.out.println("feedback");
        for (Feedback f:Feedback.feedback){
            if (f.getProf().equals(email)){
                System.out.println(f.getFeedback());
            }
        }
    }
    public void assignTA(String code, String email){
        for (Course course:all){
            if (course.getCode().equals(code)){
                    course.setTA(email);
                    System.out.println("TA assigned!");
                    return;
            }
        }
        System.out.println("course not found.");
    }
    public void updateCourseDetails(String code, String location, String timings){
        for (Course course:all){
            if (course.getCode().equals(code)){
                course.setLocation(location);
                course.setTimings(timings);
                System.out.println("course details updated successfully!");
                return;
            }
        }
        System.out.println("course not found.");
    }
}
class Student extends User{
	public Student(String email){
        super(email);
	}
	public String grade;
    public int sgpa;
    public int cgpa;
    private ArrayList<Course> registered=new ArrayList<>();  
    private ArrayList<Course> completed=new ArrayList<>();
    private ArrayList<Complaint> complaints=new ArrayList<>();
    public void viewCourses(){
        System.out.println("available courses:");
        for (Course course:all){
            System.out.println(course.getCourse());
        }
    }
    public void register(String code, int sem) throws CourseFullException{
        for (Course course:all){
            if (course.getCode().equals(code) && course.getSem() == sem){
                if (course.capacity<1){
                    throw new CourseFullException();
                }
                else{
                    if (course.getPrerequisite()!=null){
                        for (Course j:completed){
                            if (course.getPrerequisite().equals(j)){
                                registered.add(course);
                                course.addStudent(this.email);
                                course.capacity--;
                                System.out.println("registered!");
                                return;
                            }
                        }
                    }
                    else{
                        registered.add(course);
                        course.addStudent(this.email);
                        course.capacity--;
                        System.out.println("registered!");
                        return;
                    }
                }
            }
        }
        System.out.println("course not found.");
    }
    public void drop(String code) throws DropDeadlinePassedException{
        for (Course course:registered){
            if (course.getCode().equals(code)){
                if (course.daysLefttoDrop>=0){
                    registered.remove(course);
                    course.removeStudent(this.email);
                    course.capacity++;
                    System.out.println("dropped course!");
                    return;
                }
                else{
                    throw new DropDeadlinePassedException();
                }
            }
        }
        System.out.println("course not found in your registered list.");
    }
    public void fileComplaint(String description){
        complaints.add(new Complaint(this.email, description));
        System.out.println("complaint filed successfully.");
    }
    public void viewFiled(){
        for (Complaint c:complaints){
            System.out.println(c.getDescription());
        }
    }
    public void giveFeedback(Feedback f){
        for (Course course:registered){
            if (course.getProf().equals(f.getProf())){
                Feedback.feedback.add(f);
                System.out.println("Feedback submitted!");
                return;
            }
        }
        System.out.println("feedback given successfully.");
    }
    public void setGrade(String grade){
        this.grade=grade;
    }
    public void setSGPA(int grade){
        this.sgpa=grade;
    }
    public void setCGPA(int grade){
        this.cgpa=grade;
    }
    public String getGrade(){
        return grade;
    }
    public int getSGPA(){
        return sgpa;
    }
    public int getCGPA(){
        return cgpa;
    }
    public void viewTT(){
        System.out.println("registered courses:");
        for (Course course:registered){
            System.out.println("course: "+course.getCourse()+"\n");
            System.out.println("location: "+course.getLocation()+"\n");
            System.out.println("timings: "+course.getTimings()+"\n");
        }
    }
}
class TA extends Student{
    TA(String email){
        super(email);
    }
    public void viewGrades(ArrayList<Student> students, String email){
        for (Student student:students){
            if (student.email.equals(email)) {
                System.out.println("grade: "+student.getGrade());
                System.out.println("GPA: " + student.getSGPA());
                return;
            }
        }
        System.out.println("course/student not found.");
    }
    public void updateGrades(ArrayList<Student> students, String id, String grade, int sgpa){
        for (Student student:students){
            if (student.email.equals(id)){
                student.setGrade(grade);
                student.setSGPA(sgpa);
                System.out.println("student grade updated.");
                return;
            }
        }
        System.out.println("course/student not found.");
    }
}
class Admin extends User{
    public Admin(String email){
        super(email);
        this.password="admin123";
    }
    public int signup(){
        System.out.println("already signed up!");
        return 1;
    }
    public void viewCourses(){
        System.out.println("available courses:");
        for (Course course:all){
            System.out.println(course.getCourse());
        }
    }
    public void addCourses(String code, String name, int sem){
        all.add(new Course(code, name, sem));
        System.out.println("added course!");
    }
    public void dropCourses(String code){
        for (Course course:all){
            if (course.getCode().equals(code)){
                all.remove(course);
                System.out.println("deleted course!");
                return;
            }
        }
        System.out.println("course not found in directory.");
    }
    public void viewComplaints(){
        Complaint.viewComplaints();
    }
    public void resolveComplaint(int index){
        Complaint.resolveComplaint(index);
    }
    public void assignProf(String code, String email){
        for (Course course:all){
            if (course.getCode().equals(code)){
                    course.setProf(email);
                    System.out.println("professor assigned!");
                    return;
            }
        }
        System.out.println("course/prof not found.");
    }
    public void viewStudentRecords(ArrayList<Student> students, String email){
        for (Student student:students){
            if (student.email.equals(email)) {
                System.out.println("student record:");
                System.out.println("email: "+student.email);
                System.out.println("grade: "+student.getGrade());
                System.out.println("SGPA: " + student.getSGPA());
                System.out.println("CGPA: " + student.getCGPA());
                return;
            }
        }
        System.out.println("student not found.");
    }
    public void updateStudentRecords(ArrayList<Student> students, String email, String grade, int sgpa, int cgpa){
        for (Student student:students){
            if (student.email.equals(email)){
                student.setGrade(grade);
                student.setSGPA(sgpa);
                student.setCGPA(cgpa);
                System.out.println("student record updated.");
                return;
            }
        }
        System.out.println("Student not found.");
    }
}
class Main{
    public static void main(String[] args){
        Scanner scan=new Scanner(System.in);
        ArrayList<Student> s=new ArrayList<Student>();
        ArrayList<Prof> p=new ArrayList<Prof>();
        ArrayList<Admin> a=new ArrayList<Admin>();
        Student user=new Student("dummy");
        user.initializeCourses();
        while (true){
            user.all.get(0).daysLefttoDrop--;//for convenience of testing of this program it decrements with each iteration considered a new day
            //for the real portal, it would decrement at midnight every day instead
            System.out.println("welcome to the IIITD course registration portal!\n");
            System.out.println("1. enter\n2. exit application\n(press 1 or 2)");
            int n=scan.nextInt();
            scan.nextLine();
            if (n==2){
                System.out.println("thank you for using our portal!");
                break;
            } 
            else if (n==1){
                System.out.println("1. student/TA\n2. professor\n3. admin");
                System.out.println("4. exit application\n(press 1, 2, 3, or 4)");
                int k=scan.nextInt();
                scan.nextLine(); 
                if (k==4){
                    System.out.println("thank you for using our portal!");
                    break;
                } 
                else if (k==1){
                    System.out.print("enter email for student:");
                    String id=scan.nextLine();
                    Student student=null;
                    for (Student i:s) {
                        if (i.email.equals(id)){
                            student=i;
                            k=0;
                            System.out.print("enter password");
                            String pwd=scan.nextLine();
                            try {k=student.login(id,pwd);}
                            catch(InvalidLoginException e){
                                System.out.println(e.getMessage());
                                continue;
                            }
                        }
                    }
                    if (k==1){
                        student=new TA(id);
                        k=student.signup();
                        s.add(student);
                    }
                    if (k==0) continue;
                    System.out.println("1. view all courses\n2. register for courses\n3. drop courses");
                    System.out.println("4. view schedule\n5. track grades\n6. file complaint");
                    System.out.println("7. view complaints\n8. give feedback");
                    System.out.println("9. TA functionalities");
                    k=scan.nextInt();
                    scan.nextLine();
                    if (k==1) student.viewCourses();
                    else if (k==2){
                        System.out.print("enter course code: ");
                        String code=scan.nextLine();
                        System.out.print("enter semester: ");
                        int sem=scan.nextInt();
                        scan.nextLine();
                        try {student.register(code, sem);}
                            catch(CourseFullException e){
                                System.out.println(e.getMessage());
                                continue;
                            }
                    }
                    else if (k==3){
                        System.out.print("enter course code to drop: ");
                        String code=scan.nextLine();
                        try {student.drop(code);}
                            catch(DropDeadlinePassedException e){
                                System.out.println(e.getMessage());
                                continue;
                            }
                    }
                    else if (k==4) student.viewTT();
                    else if (k==5){
                        System.out.print("grade: "+student.getGrade());
                        System.out.print("SGPA: "+student.getSGPA());
                        System.out.print("CGPA: "+student.getCGPA());
                    }
                    else if (k==6){
                        System.out.print("enter complaint: ");
                        String code=scan.nextLine();
                        student.fileComplaint(code);
                    }
                    else if (k==7) student.viewFiled();
                    else if (k==8){
                        System.out.print("enter prof email: ");
                        String code=scan.nextLine();
                        System.out.print("rate from 1 to 5 or press 0 to give descriptive feedback: ");
                        int rate=scan.nextInt();
                        scan.nextLine();
                        if (rate==0){
                            System.out.print("enter feedback: ");
                            String h=scan.nextLine();
                            student.giveFeedback(new Feedback(code,h));
                        }
                        else{
                            System.out.print("enter rating: ");
                            int feedback=scan.nextInt();
                            student.giveFeedback(new Feedback(code,feedback));
                        }
                    }
                    else if (k==9){
                        System.out.print("enter course code: ");
                        String code=scan.nextLine();
                        for (Course course:student.all){
                            if (course.getTA().equals(id)){
                                TA t=(TA)student;
                                System.out.print("1. view student grades\n2. assign grades");
                                int x=scan.nextInt();
                                scan.nextLine();
                                if (x==1){
                                    System.out.print("enter email of student whose grade you want to view: ");
                                    String h=scan.nextLine();
                                    t.viewGrades(s,h);
                                }
                                if (x==2){
                                    System.out.print("enter email of student whose grade you want to update: ");
                                    String h=scan.nextLine();
                                    System.out.print("enter new grade: ");
                                    String i=scan.nextLine();
                                    System.out.print("enter new mark: ");
                                    int j=scan.nextInt();
                                    scan.nextLine();
                                    t.updateGrades(s,h,i,j);
                                }
                                break;
                            }
                        }
                    }
                }
                else if (k==2){
                    System.out.print("enter email for professor: ");
                    String id=scan.nextLine();
                    Prof professor=null;
                    for (Prof i:p){
                        if (i.email.equals(id)){
                            professor=i;
                            k=0;
                            System.out.print("enter password");
                            String pwd=scan.nextLine();
                            try {k=professor.login(id,pwd);}
                            catch(InvalidLoginException e){
                                System.out.println(e.getMessage());
                                continue;
                            }
                        }
                    }
                    if (k==2){
                        professor=new Prof(id);
                        k=professor.signup();
                        p.add(professor);
                    }
                    if (k==0) continue;
                    System.out.println("1. view students\n2. view courses\n3. update course details\n4. view feedback\n5. set TA");
                    k=scan.nextInt();
                    scan.nextLine();
                    if (k==1){
                        System.out.print("enter course code: ");
                        String code=scan.nextLine();
                        professor.viewStudents(code);
                    }
                    else if (k==2) professor.viewCourses();
                    else if (k==3){
                        System.out.print("enter course code: ");
                        String code=scan.nextLine();
                        System.out.print("enter course location: ");
                        String location=scan.nextLine();
                        System.out.print("enter course timings: ");
                        String timings=scan.nextLine();
                        professor.updateCourseDetails(code, location, timings);
                    }
                    else if (k==4) professor.viewFeedback();
                    else if (k==5){
                        System.out.print("enter course code: ");
                        String code=scan.nextLine();
                        System.out.print("enter TA email: ");
                        String l=scan.nextLine();
                        professor.assignTA(code, l);
                    }
                } 
                else if (k==3){
                    Admin admin=new Admin("admin@iiitd.ac.in");
                    System.out.print("enter password");
                    String pwd=scan.nextLine();
                    try {k=admin.login("admin@iiitd.ac.in",pwd);}
                    catch(InvalidLoginException e){
                        System.out.println(e.getMessage());
                        continue;
                    }
                    System.out.println("1. view all courses\n2. add courses\n3. delete courses");
                    System.out.println("4. view all complaints\n5.resolve complaints\n6. assign prof to course");
                    System.out.println("7. view student records\n8.update student records");
                    k=scan.nextInt();
                    scan.nextLine();
                    if (k==1) admin.viewCourses();
                    else if (k==2){
                        System.out.print("enter course code: ");
                        String code=scan.nextLine();
                        System.out.print("enter course name: ");
                        String name=scan.nextLine();
                        System.out.print("enter semester: ");
                        int sem=scan.nextInt();
                        scan.nextLine();
                        admin.addCourses(code, name, sem);
                    }
                    else if (k==3){
                        System.out.print("enter course code to delete: ");
                        String code=scan.nextLine();
                        admin.dropCourses(code);
                    }
                    else if (k==4) admin.viewComplaints();
                    else if (k==5){
                        System.out.print("enter complaint index: ");
                        int code=scan.nextInt();
                        admin.resolveComplaint(code);
                    }
                    else if (k==6){
                        System.out.print("enter course code: ");
                        String code=scan.nextLine();
                        System.out.print("enter prof email: ");
                        String l=scan.nextLine();
                        admin.assignProf(code, l);
                    }
                    else if (k==7){
                        System.out.print("enter student email: ");
                        String email=scan.nextLine();
                        admin.viewStudentRecords(s, email);
                    }
                    else if (k==8){
                        System.out.print("enter student email: ");
                        String email=scan.nextLine();
                        System.out.print("enter grade: ");
                        String grade=scan.nextLine();
                        System.out.print("enter SGPA: ");
                        int sgpa=scan.nextInt();
                        System.out.print("enter CGPA: ");
                        int cgpa=scan.nextInt();
                        admin.updateStudentRecords(s, email, grade, sgpa, cgpa);
                    }
                } 
                else{
                    System.out.println("press 1, 2, 3, or 4");
                }
            } 
            else{
                System.out.println("Press 1 or 2");
                continue;
            }
        }
        scan.close();
    }
}
