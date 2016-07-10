from contact_app.models import Contact

tmp = ['', '1990-01-02', 13312341234, 'wuhan']
i = 0
while i < 4000:
    tmp[0] = 'tony' + str(i)
    c = Contact(name=tmp[0], birthday=tmp[1], number=tmp[2], address=tmp[3])
    c.save()
    i += 1
    print "add %s %s %s %s successful" % (tmp[0], tmp[1], tmp[2], tmp[3])


