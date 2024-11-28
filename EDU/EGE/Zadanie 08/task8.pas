##
var count := 0;
foreach var d1 in '123456789ab' do
  foreach var d2 in '0123456789ab' do
    foreach var d3 in '0123456789ab' do
      foreach var d4 in '0123456789ab' do
        foreach var d5 in '0123456789ab' do
        begin
          var number :=d1+d2+d3+d4+d5;
          if number.CountOf('7')=1 then
           if number.CountOf('9')+
              number.CountOf('a')+
              number.CountOf('b')<=3 then count+=1;
        end;
        print(count)