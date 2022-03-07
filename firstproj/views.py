from django.shortcuts import render
def studentInterface(request):
       return render(request,"student.html")

def studentResult(request):
    stored_rollno = request.GET['rollno']
    stored_name = request.GET['sName']
    stored_dob = request.GET['dob']
    stored_gender = request.GET['gender']
    stored_fname = request.GET['fname']
    stored_hindi = int(request.GET['h'])
    stored_english = int(request.GET['e'])
    stored_math = int(request.GET['m'])
    stored_physics = int(request.GET['p'])
    stored_chemistry = int(request.GET['c'])

    if(stored_gender=="male"):
        pre="Mr."
        post="S/O"
    else:
        pre="Miss"
        post="D/O"


    total=stored_hindi+stored_english+stored_math+stored_physics+stored_chemistry
    per=total*100/500
    if(per<=100 and per>=60):
        div="first devision"
    elif(per<=59 and per>=45):
        div="second division"
    elif(per<=44 and per>=33):
        div="third division"
    else:
        div="fail"


    return render(request,"result.html",{'send_to_result_rollno':stored_rollno,'send_to_result_name':stored_name,'send_to_result_dob':stored_dob,'send_to_result_gender':stored_gender,'send_to_result_fname':stored_fname,'send_to_result_hindi':stored_hindi,'send_to_result_english':stored_english,'send_to_result_math':stored_math,'send_to_result_physics':stored_physics,'send_to_result_chemistry':stored_chemistry,'pre':pre,'post':post,'div':div,'total':total,'per':per})