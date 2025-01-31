<h5 id="들어가며">들어가며</h5>
<p>오늘은 쉽게 풀릴 것 같아 잠시 설렜지만, 넵 아니었습니다!</p>
<h2 id="문제">문제</h2>
<p><a href="https://www.acmicpc.net/problem/1697">백준1697 - 숨바꼭질</a>
<img alt="" src="https://velog.velcdn.com/images/edocnuyh/post/f1e5393e-1ff1-4d28-a4b4-2282636e86b1/image.png" /></p>
<br />

<h2 id="몸으로-부딪쳐-보기">몸으로 부딪쳐 보기</h2>
<p>어제 DFS, BFS에 대해 공부할 때 아 이번주 주제는 DFS, BFS겠구나라고 생각했었다. 근데 문제를 보니 이게.. 그래프? 하는 생각이 들었다. 수빈이가 점 하나고(Node), 동생이 찾아가는 위치인 건 알겠는데, 어떻게 그려야 <code>그래프</code> 자료구조 처럼 보일지 바로 떠오르지 않았다. 그래서 그냥 노트 위에다 생각나는 대로 끄적거려 보았다.</p>
<p><img height="40%" src="https://velog.velcdn.com/images/edocnuyh/post/1a3a2f9d-a82d-4717-b750-064766f11e5f/image.jpeg" width="40%" /></p>

<p>이런 식으로 생각나는대로 예제를 풀어보다가, 답으로 향하는 길목(?)을 <code>5-&gt;4-&gt;8-&gt;16-&gt;17</code> 이렇게 그려보았다. 근데 이 모양이 그래프 같았다!! <code>5,4,8,16,17</code>은 <strong>정점</strong>, 그리고 그 사이의 화살표는 <strong>간선</strong>. </p>
<p>⬇️그래서 본격적으로 그래프처럼? 그려봄⬇️
<img alt="손으로-생각하기" src="https://velog.velcdn.com/images/edocnuyh/post/53f056fc-3b13-4f1f-9cea-89b499ae3c78/image.jpeg" /></p>
<p>그리다 보니까 '아! 이 문제 수빈이가 동생에게 가는 <strong>최단거리(시간)</strong>를 물어보는 거군' 하는 벼락같은 깨달음이 찾아옴.
그럼 <strong>BFS</strong>를 쓰자! 하며 해피해피했다. </p>
<br />

<h2 id="코드로-작성해-보기">코드로 작성해 보기</h2>
<h3 id="첫-시도">첫 시도</h3>
<pre><code class="language-java">public class Main {

    // bfs!!
    public static Queue&lt;Integer&gt; queue;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        bfs(sc.nextInt(), sc.nextInt());
    }

    // bfs는 queue로 구현.
    static void bfs(int n, int k) {
        boolean[] visited = new boolean[k+1];
        visited[n] = true;

        queue = new LinkedList&lt;&gt;();
        queue.add(n);
        int time = 0;
        while (!visited[k]) { // k를 방문하면 종료
            time++;
            int node = queue.poll();
            search(visited, node-1);
            search(visited, node+1);
            search(visited, node*2);
        }

        System.out.println(time);
    }

    static void search(boolean[] visited, int node) {
        if (!visited[node]) {
            queue.add(node);
            visited[node] = true;
        }
    }
}</code></pre>
<p>처음에는 이렇게 코드를 짜보았음. 근데 이 코드에는 여러 실패지점이 있었다.</p>
<h4 id="1-방문지점-배열-visited의-크기">1. 방문지점 배열 visited의 크기</h4>
<p>아무 생각없이 동생의 위치 k를 배열의 크기로 잡았다. (k+1로 한건 그냥 인덱스 값 그대로 visited를 체크하고 싶어서 그랬음)
근데 시험삼아 코드를 한번 돌려보니, <code>ArrayIndexOutOfBoundsException</code>이 발생했다. 원인은 수빈이가 탐색을 하다보면, <code>2*x</code>만큼 이동하는 경우는 동생의 위치를 지나친 곳을 방문할 수 있기 때문이었다. (ex. 5-&gt;10-&gt;20 이렇게 가는 경우 동생이 위치한 17을 지나치게 된다.)</p>
<p>그럼 배열 크기를 완전 크게 잡아볼까? 하는 생각으로 <code>boolean[] visited = new boolean[Integer.MAX_VALUE]</code>도 시도해 보았는데, 이건 또 <code>OutOfMemoryError</code>가 났다 🥹</p>
<p>그래서 그냥 방문지점을 저장해두는 <code>visited</code>는 Set자료형으로 바꿨다..</p>
<h4 id="2-time-카운팅이-이상하다">2. time 카운팅이 이상하다</h4>
<p>또 아무 생각없이 숫자 카운팅은 반복문 돌때마다 하는거지!하는 생각으로 time 변수를 반복문 내부에서 증가시켜주고 있었다. 근데 돌려보니까 답이 <code>20</code>이 나왔다.. 디용.. </p>
<p>좀 더 생각 해보면, BFS를 큐로 구현해 두었기 때문에, 큐에서 꺼내온 정점이 
즉 시간(거리)는 전역 변수로서 카운팅 되어야하는 게 아니라, 각각의 노드마다 여기까지의 거리에 대한 정보를 가지고 있어야 할 것 같았다..</p>
<br />

<h3 id="큐에-거리정보까지-주는-방법이-뭘까">큐에 거리정보까지 주는 방법이 뭘까..?</h3>
<p>이 부분에 고민이 많았다. 큐 안에 단순 Integer타입을 저장하는 게 아닌, Map&lt;Integer, Integer&gt;타입을 저장해야 하나?(한다면 key: 노드의 값, value: 거리) 근데 뭔가 <code>Map</code>으로 하기에는 하나의 맵이 하나의 노드 정보만 가지고 있을거라 쓰기가 싫었다. <code>queue.poll()</code>후에 다시 keySet().get(0)으로 계속가져와주는게.. 그냥 보기싫었음... 근데 아무리 생각해도 Map말고는 모르겠다.... </p>
<p>결국은 내가 class 하나 만들어서 작성해보기로 했다.</p>
<br />

<h2 id="그런데-힝입니다🥲">그런데 힝입니다..🥲</h2>
<p>위 같은 생각을 하고, 예제 숫자로 검증 한 번 돌려보고, 아래 코드를 제출을 해 보았다!! 
<strong>⬇️🙅🏻‍♀️(정답아님)🙅🏻‍♀️⬇️</strong></p>
<pre><code class="language-java">public class Main {

    // bfs!!
    public static Queue&lt;X&gt; queue;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        bfs(sc.nextInt(), sc.nextInt());
    }

    // bfs는 queue로 구현.
    public static void bfs(int n, int k) {
        Set&lt;Integer&gt; visited = new HashSet&lt;&gt;();
        visited.add(n);

        queue = new LinkedList&lt;&gt;();
        int dis = 0;
        queue.add(new X(n,dis)); // node N 에서 시작
        while (!visited.contains(k)) { // k를 방문하면 종료
            X x = queue.poll();
            int pos = x.position;
            dis = x.distance + 1;
            search(visited, new X(pos-1, dis));
            search(visited, new X(pos+1, dis));
            search(visited, new X(pos*2, dis));
        }

        System.out.println(dis); // k 방문 했을 때의 거리 값.
    }

    // 탐색함수
    public static void search(Set&lt;Integer&gt; visited, X node) {
        if (!visited.contains(node.position)) {
            queue.add(node);
            visited.add(node.position);
        }
    }

    // 큐에 저장할 클래스를 만들어봄. 위치값과 거리값을 가진다.
    public static class X {
        int position; // 정점의 위치값
        int distance; // 시작점으로부터의 거리

        public X(int position, int distance) {
            this.position = position;
            this.distance = distance;
        }
    }
}</code></pre>
<p><strong>⬆️🙅🏻‍♀️(정답아님)🙅🏻‍♀️⬆️</strong></p>
<h3 id="몰랐던-복병--공간복잡도">몰랐던 복병 : 공간복잡도</h3>
<p>두근두근 기대를 했는데, 처음보는 결과가 나왔다. <strong>메모리 초과</strong>....😞
<img alt="신나는-메모리-초과" src="https://velog.velcdn.com/images/edocnuyh/post/0fc4df65-1f86-40ac-830f-6e4baa4043c1/image.png" /></p>
<p>문제를 다시 보니 <code>메모리 제한: 128MB</code>라고 적혀있었다. 큰건가? 작은건가? 감은 전혀 안오지만 지금 초과가 난걸 보면 작은건가? 
여태껏 한번도 신경 써본 적 없는데 이제 신경을 써야할 타이밍인가보다😞 </p>
<p><a href="https://programmers-story.tistory.com/entry/%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%A9%94%EB%AA%A8%EB%A6%AC-%EC%B4%88%EA%B3%BC-%EB%B0%9C%EC%83%9D-%EC%9D%B4%EC%9C%A0-%EB%B0%8F-%ED%95%B4%EA%B2%B0-%EB%B0%A9%EC%95%88">참고해보기..</a></p>
<blockquote>
<p><strong>[ 공간복잡도(Space Complexcity) ]</strong></p>
<ul>
<li>알고리즘 수행에 필요한 메모리 양을 평가</li>
<li>공간복잡도도 시간복잡도와 마찬가지로 주로 빅오표기법을 이용하여 나타낸다.</li>
</ul>
<p><a href="https://yoongrammer.tistory.com/79">참고해보기 - 시간 복잡도(Time Complexity) 및 공간 복잡도(Space Complexity)</a>
<a href="https://velog.io/@ydppwljg/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%8B%9C%EA%B0%84%EC%B4%88%EA%B3%BC-%EB%A9%94%EB%AA%A8%EB%A6%AC%EC%B4%88%EA%B3%BC-%ED%95%B4%EA%B2%B0%ED%95%98%EA%B8%B0">참고해보기 - 알고리즘 시간초과, 메모리초과 해결하기</a></p>
</blockquote>
<p>그렇지만 이제 졸려서 여기까지.. 정답은 찾지 못한채 일단 오늘은 마무리함</p>
<br />

<h2 id="정리">정리</h2>
<ul>
<li>BFS는 두 지점간 최단거리</li>
<li>손으로 그래프를 그려보니 좀 이해도가 올라간 기분이다 호호..</li>
<li>공간복잡도에 대해 생각해보자</li>
<li>오늘은 피곤해서 정답코드를 찾아보지 못했음.. 나중에 다시 풀어보기!</li>
<li>아직은 BFS랑 안친함.</li>
</ul>