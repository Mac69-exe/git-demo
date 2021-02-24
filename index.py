export GOROOT=/usr/local/go
export GOPATH=$HOME/go
export PATH=$GOPATH/bin:$GOROOT/bin:$PATH



sublist3r( ){
python3 ~/tools/Sublist3r/sublist3r.py -d $1 -t 50

}

drishati() {
python3 ~/tools/gaussrf/Drishti/drishti.py $1
}
