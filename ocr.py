import sys
import tr

if len(sys.argv) < 3:
    exit(0)
else:
    print(sys.argv[1])
    lines=tr.run(sys.argv[1])
    with open(sys.argv[2],'a') as f:
        f.write('\n'+sys.argv[1]+'\n')
        for line in lines:
            if len(line[1])>0:
                print(line[1], len(line[1]))
                f.write(line[1])
                if len(sys.argv)==3:
                    f.write("\n")
                    if len(line[1]) < 20:
                        f.write("\n")
                elif len(line[1]) < int(sys.argv[3]):
                    f.write("\n\n")
