class Solution {
    public String solution(String myString) {
        StringBuilder sb = new StringBuilder();
        for(int i=0; i<myString.length(); i++){
            if(myString.charAt(i) < 'l'){
                sb.append('l');
            }else{
                sb.append(myString.charAt(i));
            }
        }
        String answer = sb.toString();
        
        return answer;
    }
}

/*
def solution(myString):
    answer = ''
    for i in myString:
        if i< 'l':
            answer+='l'
        else:
            answer+=i
    return answer
*/
