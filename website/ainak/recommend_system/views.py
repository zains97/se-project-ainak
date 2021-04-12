from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.contrib.auth.hashers import make_password, check_password
# from django.contrib.sessions.models import Session
import datetime
import numpy as np

from imutils.video import VideoStream
from imutils import face_utils
import imutils
import time
import dlib
from cv2 import cv2


# Create your views here.
def index(request):
    sunglasses = Home.objects.filter(category="sunglasses").count()
    eyeglasses = Home.objects.filter(category="eyeglasses").count()
    return render(request, 'recommend_system/index.html',
                      {'sunglasses': sunglasses, 'eyeglasses': eyeglasses})

def search(request):
    if request.method == "POST":
        search = request.POST.get('search_text')
        if not search.isdigit():
            fetch_data = Home.objects.filter(Q(city__icontains=search) | Q(location__icontains=search) | Q(price__icontains=search) | Q(sft__icontains=search) | Q(category__icontains=search))
            return render(request, 'recommend_system/search.html', {'data': fetch_data})
        else:
            fetch_data = Home.objects.filter(Q(price__icontains=search) | Q(price__lte=search) | Q(sft__icontains=search))
            return render(request, 'recommend_system/search.html', {'data': fetch_data})

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        fname = request.POST.get('fname', '')
        lname = request.POST.get('lname', '')
        email = request.POST.get('email', '')
        city = request.POST.get('city', '')
        pass1 = request.POST.get('pass1', '')
        pass2 = request.POST.get('pass2', '')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken, Please Try Again!")
            return redirect('Home')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already taken, Please Try Again!")
            return redirect('Home')

        if len(username) > 20:
            messages.error(request, "Username must be under 20 charcaters")
            return redirect('Home')

        if not username.isalnum():
            messages.error(request, "Username should only contain Letters and Numbers")
            return redirect('Home')

        if pass1 != pass2:
            messages.error(request, "Password do no match!")
            return redirect('Home')

        data = User(username=username, fname=fname, lname=lname, email=email, city=city, pass1=pass1, pass2=pass2)
        data.save()
        messages.success(request, "Your Account has been successfully Completed")
        return redirect('Home')

    else:
        return render(request, 'recommend_system/index.html')

def login(request):
    if request.session.has_key('is_logged'):
        return redirect('Home')
    if request.method == "POST":
        loginusername = request.POST.get('loginusername', '')
        loginpass = request.POST.get('loginpass', '')
        request.session['user'] = request.POST.get('user')

       # loginpass1 = check_password(loginpass, User.pass1)

        if request.session['user'] == 'Consumer':
            count = User.objects.filter(username=loginusername, pass1=loginpass).count()
            if count > 0:
                request.session['is_logged'] = loginusername

                # request.session['user_id'] = request.session['is_logged'].id
                request.session['user_id'] = User.objects.values('id').filter(username=loginusername, pass1=loginpass)[0]['id']
                request.session['user_email'] = User.objects.values('email').filter(username=loginusername, pass1=loginpass)[0]['email']

                if request.COOKIES.get('logged') == True:
                    return HttpResponse("1 - User is logged in")
                else:
                    messages.success(request, "You have succuessfully Login")
                    response = redirect('Home')
                    response.set_cookie(request.session['is_logged'], datetime.datetime.now())

                    return response

               # return render(request, 'recommend_system/index.html', {"loginusername": loginusername})

            else:
                messages.error(request, "Invalid Credentials, Please Try Again!")
                return redirect('Home')

        elif request.session['user'] == 'Admin':
            count = Admin.objects.filter(username=loginusername, pass1=loginpass).count()
            if count > 0:
                request.session['is_logged'] = loginusername

                # request.session['user_id'] = request.session['is_logged'].id
                request.session['user_id'] = Admin.objects.values('id').filter(username=loginusername, pass1=loginpass)[0]['id']
                request.session['user_email'] = Admin.objects.values('email').filter(username=loginusername, pass1=loginpass)[0]['email']

                if request.COOKIES.get('logged') == True:
                    return HttpResponse("1 - User is logged in")
                else:
                    messages.success(request, "You have succuessfully Login")
                    response = redirect('dashboard')
                    response.set_cookie(request.session['is_logged'], datetime.datetime.now())

                    return response

               # return render(request, 'recommend_system/index.html', {"loginusername": loginusername})

            else:
                messages.error(request, "Invalid Credentials, Please Try Again!")
                return redirect('Home')

    if request.session.has_key('is_logged'):
        return render(request, 'recommend_system/index.html')
    return redirect('Home')

def logout(request):
    if request.session.has_key('is_logged'):
        del request.session['is_logged']
    return redirect('Home')

def sunglasses(request):
    homes = Home.objects.filter(category="sunglasses").order_by('-id')
    paginator = Paginator(homes, 9)
    page = request.GET.get('page')
    homes = paginator.get_page(page)

    return render(request, 'recommend_system/sunglasses.html', {'homes': homes})

def eyeglasses(request):
    homes = Home.objects.filter(category="eyeglasses").order_by('-id')
    paginator = Paginator(homes, 9)
    page = request.GET.get('page')
    homes = paginator.get_page(page)

    return render(request, 'recommend_system/eyeglasses.html', {'homes': homes})

def vissiontest(request):
    return render(request, 'recommend_system/vissiontest.html')

def transparent_overlay(src, overlay, x, y, scale=1):
    src = src.copy()
    overlay = cv2.resize(overlay, (0, 0), fx=scale, fy=scale)
    h, w, _ = overlay.shape  # Size of foreground
    rows, cols, _ = src.shape  # Size of background Image

    # loop over all pixels and apply the blending equation
    for i in range(h):
        for j in range(w):
            if y + i >= rows or x + j >= cols:
                continue
            alpha = float(overlay[i][j][3] / 255.0)  # read the alpha channel
            src[y + i][x + j] = alpha * overlay[i][j][:3] + (1 - alpha) * src[y + i][x + j]
    return src


def watermarking(original, watermarked, alpha=1, x=0, y=0):
    overlay = transparent_overlay(original, watermarked, x, y)
    output = original.copy()
    cv2.addWeighted(overlay, 1, output, 1 - 1, 0, output)
    return output

def glassesdetail(request, myid):
    post_id = myid

    data = Home.objects.filter(id=post_id)
    for i in data:
        image = i.landscape1
   # ii = "recommend_system/data/glass5.png"
    ii = "media/" + str(image)

    if 'virtual' in request.POST:
        print("[INFO] loading facial landmark predictor...")
        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor("recommend_system/shape_predictor_68_face_landmarks.dat")

        print("[INFO] camera sensor warming up...")
        vs = VideoStream(0).start()
        time.sleep(2.0)
        glass = cv2.imread(ii, cv2.IMREAD_UNCHANGED)

       # moustache = cv2.imread("recommend_system/data/moustache.png", cv2.IMREAD_UNCHANGED)

        # loop over the frames from the video stream
        while True:
            # grayscale
            frame = vs.read()
            frame = imutils.resize(frame, height=550)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # detect faces in the grayayscale frame
            rects = detector(gray, 0)

            # loopop over found faces
            for rect in rects:
                shape = predictor(frame, rect)
                shape = face_utils.shape_to_np(shape)

                eyeLeftSide = 0
                eyeRightSide = 0
                eyeTopSide = 0
                eyeBottomSide = 0

                # moustacheLeftSide = 0
                # moustacheRightSide = 0
                # moustacheTopSide = 0
                # moustacheBottomSide = 0

                for (i, (x, y)) in enumerate(shape):
                    if (i + 1) == 37:
                        eyeLeftSide = x - 40
                    if (i + 1) == 38:
                        eyeTopSide = y - 30
                    if (i + 1) == 46:
                        eyeRightSide = x + 40
                    if (i + 1) == 48:
                        eyeBottomSide = y + 30

                    # if (i + 1) == 2:
                    #     moustacheLeftSide = x
                    #     moustacheTopSide = y - 10
                    # if (i + 1) == 16:
                    #     moustacheRightSide = x
                    # if (i + 1) == 9:
                    #     moustacheBottomSide = y

                eyesWidth = eyeRightSide - eyeLeftSide
                if eyesWidth < 0:
                    eyesWidth = eyesWidth * -1

                # add glasses
                fitedGlass = imutils.resize(glass, width=eyesWidth)
                frame = watermarking(frame, fitedGlass, x=eyeLeftSide, y=eyeTopSide)

                # moustacheWidth = moustacheRightSide - moustacheLeftSide
                # if moustacheWidth < 0:
                #     moustacheWidth = moustacheWidth * -1
                #
                # # add moustache
                # fitedMoustache = imutils.resize(moustache, width=moustacheWidth)
                # frame = watermarking(frame, fitedMoustache, x=moustacheLeftSide, y=moustacheTopSide)

            # cv2.imshow("Glass", fitedGlass)
            key = cv2.waitKey(1) & 0xFF

            # if the `q` key was pressed, break from the loop
            if key == ord("q"):
                break

            # show the frame
            cv2.imshow("Face Mask", frame)

        # do a bit of cleanup
        cv2.destroyAllWindows()
        vs.stop()

    if 'l_click_item' in request.POST:
        home = Home.objects.filter(id=myid)
        comment = Comment.objects.all().filter(post_id=myid)
        return render(request, 'recommend_system/glassesdetail.html',
                      {'home': home[0], 'comments': comment})

    if request.session.has_key('is_logged'):
        user_id = request.session['user_id']
        if request.method == "POST":
            # If click on property user data and id goes to "click_item" table
            if 'click_item' in request.POST:
                user_id = request.POST.get('user_id')
                post_id = myid
                email = request.POST.get('email')

                qurey = Click_item(email=email)
                qurey.user_id_id = user_id
                qurey.post_id_id = post_id
                qurey.save()
            # End Click_Item Function

            # If you Commment on property then it will save on "Comment" table
            elif 'commment' in request.POST:
                message = request.POST.get('message')
                user_id = request.POST.get('user_id')
                post_id = myid

                qurey = Comment(message=message)
                qurey.post_id_id = post_id
                qurey.user_id_id = user_id
                qurey.save()
            # End Comment Function

            # If you Rate any property, Rating will saved in "Rating" table
            elif 'rating' in request.POST:
                rating = request.POST.get('rating')
                user_id = user_id
                post_id = post_id

                qurey = Rating(rating=rating)
                qurey.post_id_id = post_id
                qurey.user_id_id = user_id
                qurey.save()
            # End Rating Function

            # If you add properties in wishlist, it will saved in "WishList" table
            elif 'wishlist' in request.POST:
                user_id = request.POST.get('user_id')
                post_id = myid
                email = request.POST.get('email')

                qurey = Wish_list(email=email)
                qurey.user_id_id = user_id
                qurey.post_id_id = post_id
                qurey.save()
            # End WishList Function


            elif 'remove' in request.POST:
                delete = Wish_list.objects.filter(user_id=user_id, post_id=myid)
                delete.delete()

            elif 'buy' in request.POST:
                user_id = request.POST.get('user_id')
                post_id = myid
                address = request.POST.get('address')
                righteye = request.POST.get('righteye')
                lefteye = request.POST.get('lefteye')

                qurey = Buy(address=address, reye=righteye, leye=lefteye)
                qurey.user_id_id = user_id
                qurey.post_id_id = post_id
                qurey.save()


            elif 'cancel' in request.POST:
                delete = Buy.objects.filter(user_id=user_id, post_id=myid)
                delete.delete()

            check_buy = Buy.objects.filter(user_id=user_id, post_id=post_id)
            check = Wish_list.objects.filter(user_id=user_id, post_id=post_id)
            rating_check = Rating.objects.filter(user_id=user_id, post_id=post_id)
            comment = Comment.objects.all().filter(post_id=myid)
            home = Home.objects.filter(id=myid)

            return render(request, 'recommend_system/glassesdetail.html',
                          {'rating_check': rating_check, 'home': home[0], 'comments': comment, 'check': check, 'check_buy': check_buy})

    home = Home.objects.filter(id=myid)
    comment = Comment.objects.all().filter(post_id=myid)
    return render(request, 'recommend_system/glassesdetail.html',
                      {'home': home[0], 'comments': comment})

    #return render('request', 'recommend_system/propertydetail.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
    return render(request, 'recommend_system/contact.html')

def sell(request):
    if request.session.has_key('is_logged'):
        if request.method == "POST":
            if 'sell' in request.POST:
                city = request.POST.get('city')
                location = request.POST.get('location')
                category = request.POST.get('category')
                status = request.POST.get('status')
                price = request.POST.get('price')
                sft = request.POST.get('sft')
                user_id = request.POST.get('user_id')
                name = request.POST.get('name')
                email = request.POST.get('email')
                description = request.POST.get('description')

                profile = Home(city=city, location=location, category=category, status=status, price=price, sft=sft, name=name, email=email, description=description)
                profile.portrait = request.FILES.get('displayimg')
                profile.landscape1 = request.FILES.get('img1')
                profile.landscape2 = request.FILES.get('img2')
                profile.landscape3 = request.FILES.get('img3')
                profile.landscape4 = request.FILES.get('img4')
                profile.landscape5 = request.FILES.get('img5')
                profile.save()

        return render(request, 'recommend_system/sell.html')
    return redirect("Home")

def account(request, id):
    if request.session.has_key('is_logged'):
        if request.method == "POST":
            if 'account' in request.POST:
                update = User.objects.get(id=id)
                update.fname = request.POST.get('fname', '')
                update.lname = request.POST.get('lname', '')
                update.email = request.POST.get('email', '')
                update.city = request.POST.get('city', '')
                update.pass1 = request.POST.get('pass1', '')
                update.pass2 = request.POST.get('pass2', '')
                update.datetime = datetime.now()

                if request.POST.get('pass1', '') != request.POST.get('pass2', ''):
                    messages.error(request, "Password do no match!")
                    return redirect('account', id)

                update.save()
                messages.success(request, "Your Account information has been successfully Updated")
                return redirect('account', id)

        data = User.objects.get(id=id)
        clickcount = Click_item.objects.filter(user_id=id).count()
        wishcount = Wish_list.objects.filter(user_id=id).count()
        buy = Buy.objects.filter(user_id=id).count()
        return render(request, 'recommend_system/account.html', {'data': data, 'clickcount': clickcount, 'wishcount': wishcount, 'buy': buy})
    return redirect("Home")

def viewglasses(request, id):
    if request.session.has_key('is_logged'):
        if request.method == "POST":
            dealerid = request.POST.get('id')
            delete = Click_item.objects.get(id=dealerid)
            delete.delete()

        data = Click_item.objects.filter(user_id=id).order_by('-id')

        paginator = Paginator(data, 9)
        page = request.GET.get('page')
        data = paginator.get_page(page)

        clickcount = Click_item.objects.filter(user_id=id).count()
        wishcount = Wish_list.objects.filter(user_id=id).count()
        buy = Buy.objects.filter(user_id=id).count()
        return render(request, 'recommend_system/viewglasses.html', {'data': data, 'clickcount': clickcount, 'wishcount': wishcount, 'buy': buy})
    return redirect("Home")

def wishlist(request, id):
    if request.session.has_key('is_logged'):
        if request.method == "POST":
            dealerid = request.POST.get('id')
            delete = Wish_list.objects.get(id=dealerid)
            delete.delete()

        data = Wish_list.objects.filter(user_id=id).order_by('-id')

        paginator = Paginator(data, 9)
        page = request.GET.get('page')
        data = paginator.get_page(page)

        wishcount = Wish_list.objects.filter(user_id=id).count()
        clickcount = Click_item.objects.filter(user_id=id).count()
        buy = Buy.objects.filter(user_id=id).count()
        return render(request, 'recommend_system/wishlist.html', {'data': data, 'wishcount': wishcount, 'clickcount': clickcount, 'buy': buy})
    return redirect("Home")

def buy(request, id):
    if request.session.has_key('is_logged'):
        if request.method == "POST":
            id = request.POST.get('id')
            delete = Buy.objects.get(id=id)
            delete.delete()

        data = Buy.objects.filter(user_id=id).order_by('-id')
        clickcount = Click_item.objects.filter(user_id=id).count()
        wishcount = Wish_list.objects.filter(user_id=id).count()
        buy = Buy.objects.filter(user_id=id).count()
        return render(request, 'recommend_system/buy.html', {'data': data, 'clickcount': clickcount, 'wishcount': wishcount, 'buy': buy})
    return redirect("Home")

def about(request):
    return render(request, 'recommend_system/about.html')

def dashboard(request):
    if request.session.has_key('is_logged'):
        user_id = request.session['user_id']
        if request.method == "POST":
            if 'update' in request.POST:
                update = Admin.objects.get(id=user_id)
                update.username = request.POST.get('username', '')
                update.email = request.POST.get('email', '')
                update.pass1 = request.POST.get('pass1', '')
                update.save()
                messages.success(request, "Your Account information has been successfully Updated")
                return redirect('dashboard')

            elif 'addemployee' in request.POST:
                username = request.POST.get('username', '')
                email = request.POST.get('email', '')
                pass1 = request.POST.get('pass1', '')

                if Admin.objects.filter(username=username).exists():
                    messages.error(request, "Username already taken, Please Try Again!")
                    return redirect('dashboard')

                if Admin.objects.filter(email=email).exists():
                    messages.error(request, "Email already taken, Please Try Again!")
                    return redirect('dashboard')

                if len(username) > 20:
                    messages.error(request, "Username must be under 20 charcaters")
                    return redirect('dashboard')

                if not username.isalnum():
                    messages.error(request, "Username should only contain Letters and Numbers")
                    return redirect('dashboard')

                data = Admin(username=username, email=email, pass1=pass1)
                data.save()
                messages.success(request, "Successfully Added")
                return redirect('dashboard')

            elif 'adduser' in request.POST:
                username = request.POST.get('username', '')
                fname = request.POST.get('fname', '')
                lname = request.POST.get('lname', '')
                email = request.POST.get('email', '')
                city = request.POST.get('city', '')
                pass1 = request.POST.get('pass1', '')
                pass2 = request.POST.get('pass2', '')

                if User.objects.filter(username=username).exists():
                    messages.error(request, "Username already taken, Please Try Again!")
                    return redirect('dashboard')

                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email already taken, Please Try Again!")
                    return redirect('dashboard')

                if len(username) > 20:
                    messages.error(request, "Username must be under 20 charcaters")
                    return redirect('dashboard')

                if not username.isalnum():
                    messages.error(request, "Username should only contain Letters and Numbers")
                    return redirect('dashboard')

                if pass1 != pass2:
                    messages.error(request, "Password do no match!")
                    return redirect('dashboard')

                data = User(username=username, fname=fname, lname=lname, email=email, city=city, pass1=pass1,
                            pass2=pass2)
                data.save()
                messages.success(request, "Your Account has been successfully Completed")
                return redirect('dashboard')


        data = Admin.objects.get(id=user_id)
        return render(request, 'recommend_system/dashboard.html', {'data': data} )
    return redirect("Home")


def delivery(request):
    data = Buy.objects.all().order_by('-id')
    return render(request, 'recommend_system/delivery.html', {'data': data})

def allusers(request):
    data = User.objects.all().order_by('-id')
    return render(request, 'recommend_system/users.html', {'data': data})