<h5 id="들어가며">들어가며</h5>
<p>2주차! 새로운 개념! 익혀보자..</p>
<h2 id="문제">문제</h2>
<p><a href="https://www.acmicpc.net/problem/1260">백준1260 - DFS와 BFS</a>
<img alt="백준1260 - DFS와 BFS" src="https://velog.velcdn.com/images/edocnuyh/post/fc1561b4-3567-41f0-92df-b316d78da91f/image.png" /></p>
<br />

<h2 id="dfs-bfs-그게-뭔데-😠">DFS, BFS 그게 뭔데 😠</h2>
<p><a href="https://devuna.tistory.com/32">참고블로그1</a>
<a href="https://velog.io/@juliajh/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B9%8A%EC%9D%B4-%EC%9A%B0%EC%84%A0-%ED%83%90%EC%83%89DFS%EA%B3%BC-%EB%84%88%EB%B9%84-%EC%9A%B0%EC%84%A0-%ED%83%90%EC%83%89BFS">참고블로그2</a>
기본적으로 내가 너무 무지랭이라 ㅎㅎ 문제를 보고 오늘은 그냥 개념을 익히는 시간을 가져야겠다고 판단했다. 그래서 일단 익혀본다~ 🍳</p>
<blockquote>
<p><strong>잠깐~ 먼저 알아 둬야 할 것</strong>
DFS, BFS는 _그래프_를 탐색할 때 사용하는 방법이다. 그럼 먼저 _그래프_가 뭔지 알아야함 흑흑🥹</p>
<p><strong>[ 그래프? ]</strong>
정점(node)과 그 정점들을 연결하는 간선(edge)로 이루어진 자료구조.
그래프를 탐색한다 &gt; 하나의 정점에서 시작(start)해서 모든 정점들을 한 번씩 <strong>방문</strong>(visit)하는 것.</p>
</blockquote>
<h3 id="-dfs-깊이-우선-탐색depth-first-search-">[ DFS: 깊이 우선 탐색(Depth-First-Search) ]</h3>
<p><strong>특정노드에서 시작해서 다음 분기로 넘어가기 전에 해당 분기를 완벽하게 탐색하는 방법이다.</strong>
<img alt="출처 - https://developer-mac.tistory.com/64" src="https://upload.wikimedia.org/wikipedia/commons/7/7f/Depth-First-Search.gif" />
이름처럼 땅굴을 파고 들어가는 탐색법. 깊게 깊게 들어간다.
한 브랜치만 끝까지 파는 탐색법이다. <del>한 놈 다 패고 나서 다음 놈 패기.</del></p>
<h3 id="-bfs-너비-우선-탐색breadth-first-search-">[ BFS: 너비 우선 탐색(Breadth-First-Search) ]</h3>
<p>특정노드에서 시작해서 <strong>인접한 노드</strong>를 먼저 탐색하는 방법
<img alt="출처 - https://developer-mac.tistory.com/64" src="https://upload.wikimedia.org/wikipedia/commons/5/5d/Breadth-First-Search-Algorithm.gif" />
대충 용어는 모르겠지만.. 시작한 노드를 중심으로 가까운 애들부터.. 탐색. 걍 옆으로 탐색한다고 생각하자.</p>
<br />


<p>아래부분은 추후작성..</p>
<h2 id="그래서-구현은-어떻게-하는데">그래서 구현은 어떻게 하는데</h2>
<h3 id="그래프">그래프?</h3>
<h3 id="dfs---왜-stack">DFS - 왜 Stack?</h3>
<h3 id="bfs---왜-queue">BFS - 왜 Queue?</h3>
<h3 id="재귀함수">재귀함수?</h3>
<br />

<h2 id="최종제출코드">최종제출코드</h2>
<pre><code class="language-java">public class Main {

    // 입력 : n, m, v, loop: a,b
    public static int n, m, v, a, b;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        v = sc.nextInt();

        int[][] edges = new int[n + 1][n + 1];
        // 간선의 개수 만큼 반복
        for (int i = 0; i &lt; m; i++) {
            a = sc.nextInt();
            b = sc.nextInt();
            edges[a][b] = 1;
            edges[b][a] = 1;
        }

        dfs(edges, v);
        bfs(edges, v);
    }

    // 깊이 우선 탐색! 아래로~
    static void dfs(int[][] edges, int startV) {
        boolean[] visited = new boolean[n+1];
        Stack&lt;Integer&gt; stack = new Stack&lt;&gt;();
        StringBuilder sb = new StringBuilder();

        stack.push(startV);
        while (!stack.isEmpty()) {
            int node = stack.pop();

            if (!visited[node]) {
                visited[node] = true;
                sb.append(node).append(' ');

                for (int i = n; i &gt; 0 ; i--) {
                    if (edges[node][i] == 1 &amp;&amp; !visited[i]) {
                        stack.push(i);
                    }
                }
            }
        }

        System.out.println(sb);
    }

    // 너비 우선 탐색! 옆으로~
    static void bfs(int[][] edges, int startV) {
        boolean[] visited = new boolean[n+1];
        Queue&lt;Integer&gt; queue = new LinkedList&lt;&gt;();

        queue.add(startV);
        visited[startV] = true;

        StringBuilder sb = new StringBuilder();
        while (!queue.isEmpty()) {
            int node = queue.poll();
            sb.append(node).append(' ');
            for (int i = 1; i &lt;= n; i++) {
                if (edges[node][i] == 1 &amp;&amp; !visited[i]) {
                    queue.add(i);
                    visited[i] = true;
                }
            }
        }

        System.out.println(sb);
    }
}</code></pre>
<br />


<h2 id="정리">정리</h2>
<ul>
<li>동그란건 정점이오, 이어주는건 간선이로다</li>
<li>DFS(Depth): 깊이 우선, 땅굴파기</li>
<li>BFS(Breadth): 너비 우선, 옆으로</li>
</ul>