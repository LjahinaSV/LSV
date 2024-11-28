##
var a:='0123456789ab'.Cartesian(5)
.Where(n -> n.First<>'0')
.Where(n -> n.CountOf('7')=1)
.Where(n->n.CountOf('9')+n.CountOf('a')+n.CountOf('b')<=3)
.Count.print