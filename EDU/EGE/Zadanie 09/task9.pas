begin
  var a:=readlines('9_.txt');
  var count:=0;
  var l1:=new List<integer>; var l3:=new List<integer>;
  foreach var x in a do
  begin
    var l:=x.ToIntegers.ToList;
    foreach var i in l do
    begin
      if l.countOf(i)=3 then l3.add(i);
      if l.countOf(i)=1 then l1.add(i);
      if (l3.count=3) and (l1.count=3) then
        if l3.sum**2>l1.sum**2 then count+=1;
    end;
    l3.Clear;l1.Clear;
  end;
  print(count);
end.