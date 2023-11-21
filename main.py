import functions

func = functions.Function()

cmnd = func.recognize()
fname = ""

if cmnd[0] == "start":
    apptype = cmnd[1]
    appname = cmnd[-1]
    #appname = func.name(cmnd)
    func.start(appname, apptype)

if cmnd[0] == "open":
    ftype = cmnd[1].lower()
    if "from" in cmnd:
        ind = cmnd.index("from")
        fname = fname + f"{cmnd[ind + 1]}:"
        for x in range(ind+2, len(cmnd)):
            fname = fname + f"{cmnd[x]}\\"
        fname = fname + cmnd[2]

    # else:
    #     fname = func.name(cmnd)
    # func.open(fname, ftype)
