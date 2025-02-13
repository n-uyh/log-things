<h5 id="들어가며">들어가며</h5>
<p>나.. 그리디랑 잘맞는걸지도🤭 (착각입니다)</p>
<h2 id="👿-문제">👿 문제</h2>
<p><a href="https://www.acmicpc.net/problem/11399">백준11399 - ATM</a>
<img alt="" src="https://velog.velcdn.com/images/edocnuyh/post/8dc9bc0f-b493-4162-97cf-88fb8a521ef1/image.png" /></p>
<br />

<h2 id="🧐-생각">🧐 생각</h2>
<h3 id="최솟값">최솟값?</h3>
<p>시간이 짧게 걸리는 사람부터 돈을 뽑아야 하지 않을까?</p>
<h3 id="시간의-합">시간의 합?</h3>
<p>$$
\begin{aligned}
\displaystyle\sum_{i=0}^{n}{P} &amp;= P_{1} + (P_{1} + P_{2}) + (P_{1} + P_{2} + P_{3}) + ... + (P_{1} + P_{2} + P_{3} + ...+ P_{n})\
 &amp;= (P_{1} \times n) + (P_{2} \times (n-1)) + (P_{3} \times (n-2)) + ... + (P_{n} \times 1)
\end{aligned}
$$</p>
<h3 id="합을-계산하고-보니">합을 계산하고 보니</h3>
<p>1번 사람의 시간이 $n$번 곱해지고, $n$번 사람의 시간이 1번 곱해지므로, 인출시간이 짧게 걸리는 사람부터 오름차순으로 정렬해줘야하는 것은 명확해졌다.</p>
<br />

<h2 id="📌-구현">📌 구현</h2>
<pre><code class="language-java">public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[n];
        for (int i = 0; i &lt; n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr);

        int result = 0;
        for (int i = 0; i &lt; n; i++) {
            result += arr[i] * (n-i);
        }

        System.out.println(result);
    }

}</code></pre>
<br />

<h2 id="☘️-마치며">☘️ 마치며</h2>
<h3 id="bufferedreader가-확실히-빠르다">BufferedReader가 확실히 빠르다</h3>
<p>처음에는 입력받을게 몇 개 없어보여서 <code>Scanner</code>를 사용해서 문제를 풀었다. int만 계속 받는다면 그냥 <code>Scanner</code>가 구현이 편해서 선호하는 편이기 때문이다.
근데 채점할 때 속도가 좀 느리다는 느낌이 있었고, 백준 내의 채점현황에서 속도가 빠른 분의 코드를 보니 <code>BufferedReader</code>로 구현되어 있었다.(로직자체는 엇비슷했음)
그래서 나도 <code>BufferedReader</code>로 수정해서 제출해보았더니 속도가 엄청 빨라졌다. (224ms -&gt; 112ms)
<img alt="" src="https://velog.velcdn.com/images/edocnuyh/post/77eca9fb-9e70-4b40-bfad-e095a1b4fdc3/image.png" /></p>
<h3 id="9분만에-풀었다">9분만에 풀었다..!</h3>
<img src="https://velog.velcdn.com/images/edocnuyh/post/73dbc2b2-024a-4bec-8266-846dbfc44736/image.png" style="width: 400px;" />

<p>물론 쉬운 문제 같지만, 그래도 매번 2시간 씩 걸리다가 9분만에 푸니까.. 감사감격..
더 열심히 공부해나갈 동기부여가 되는 듯하다.
앞으로도 화이팅 화이팅이다<del>~</del> 
<img alt="" src="https://velog.velcdn.com/images/edocnuyh/post/9c4ce8f4-40ff-4c7f-97d6-9a6fadb1e5a8/image.png" /></p>