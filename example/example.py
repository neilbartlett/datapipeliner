import sys
import getopt
import custom_functions
import datapipeliner as dpp

tags = []
try:
    opts, args = getopt.getopt(sys.argv[1:],"ht:",["tags="])

    for opt, arg in opts:
        if opt == '-h':
            print('example.py -t "tag1;tag2"')
            sys.exit()
        elif opt in ("-t", "--tags"):
            tags = arg.split(";")
except getopt.GetoptError:
    print('example.py -c <config.yaml> -t "tag1;tag2"')
    sys.exit(2)

src = dpp.Source("example_source")  # generate the source from `config.yaml`
snk = dpp.Sink("example_sink")  # generate the sink from `config.yaml`.

# generate the pipeline from `config.yaml`.
line = dpp.Line("example_pipeline", custom_functions, tags=tags)

# connect the source and sink to the pipeline, print what the pipeline will do, then run
# the pipeline, writing the output to disk. 
dfs_in = line.connect(src, snk)
print(line.pipeline)
dfs_out = line.run()
