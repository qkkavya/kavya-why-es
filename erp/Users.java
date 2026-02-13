import java.util.Scanner;
import java.util.ArrayList;
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