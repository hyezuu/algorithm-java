import sys
from collections import deque
input = sys.stdin.readline
# 메모리 34088KB / 시간 64ms
def bfs(x, y):
  global bug
  q = deque()
  q.append((x, y))
  visited[x][y] = True
  while q:
    curx, cury = q.popleft()
    for d in directions:
      nx, ny = curx+d[0], cury+d[1]
      if 0<=nx<m and 0<=ny<n and graph[nx][ny]== 1 and not visited[nx][ny]:
        q.append((nx, ny))
        visited[nx][ny] = True
  bug+=1

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * n for _ in range(m)]
    visited = [[False] * n for _ in range(m)]
    bug = 0
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
    print(bug)
"""
import sys
from collections import deque
input = sys.stdin.readline
# 메모리 34068KB / 시간 72ms
def bfs(x, y):
  q = deque()
  q.append((x, y))
  visited[x][y] = True
  while q:
    curx, cury = q.popleft()
    for d in directions:
      nx, ny = curx+d[0], cury+d[1]
      if 0<=nx<m and 0<=ny<n and graph[nx][ny]== 1 and not visited[nx][ny]:
        q.append((nx, ny))
        visited[nx][ny] = True

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * n for _ in range(m)]
    visited = [[False] * n for _ in range(m)]
    bug = 0
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                bug+=1
    print(bug)
"""
"""
import java.io.*;
import java.util.*;

public class Main {

    public static int m, n, bug;
    public static int[][] graph; //밭
    public static boolean[][] visited; // 벌레 방문처리

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int t = Integer.parseInt(br.readLine());
        StringTokenizer st;
        while(t>0){
            //입력 값 세팅
            st = new StringTokenizer(br.readLine());
            m = Integer.parseInt(st.nextToken());//가로
            n = Integer.parseInt(st.nextToken());//세로
            int k = Integer.parseInt(st.nextToken()); //배추 개수
            graph = new int[m][n];
            visited = new boolean[m][n];
            for(int i=0; i<k; i++){
                st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                graph[x][y] = 1;
            }
            bug = 0; //테케별 벌레 0마리 초기화
            //탐색 시작
            for(int i=0; i<m; i++){
                for(int j=0; j<n; j++){
                    //배추일 때 && 방문안한 좌표일 때
                    if(graph[i][j] == 1 && !visited[i][j]){
                        visited[i][j] = true; //방문처리
                        bfs(i, j);
                    }
                }
            }
            bw.write(bug+"\n");
            t--;
        }
        bw.flush();
        br.close();
        bw.close();
    }
    public static void bfs(int x, int y){
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{x, y});
        int[] dx = {1, 0, -1, 0};
        int[] dy = {0, 1, 0, -1};

        while(!q.isEmpty()){
            int[] cur = q.poll();
            //인접한 좌표 탐색
            for(int i=0; i<4; i++){
                int nx = cur[0] + dx[i];
                int ny = cur[1] + dy[i];
                //인접한 좌표가 범위 밖일 경우 skip
                if(nx<0 || nx>=m || ny<0 || ny>=n) continue;
                //이미 방문한 좌표거나 배추가 없는 땅일 경우 skip
                if(visited[nx][ny]||graph[nx][ny]==0) continue;
                visited[nx][ny] = true;
                q.offer(new int[]{nx, ny});
            }
        }
        bug++; //벌레 개수 증가
    }
}
"""
