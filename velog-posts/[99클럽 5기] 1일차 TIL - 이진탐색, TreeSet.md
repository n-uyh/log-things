<h5 id="들어가며">들어가며</h5>
<p><del>(주의!) 이 글은 일기에 가까우며, 매우 의식의 흐름대로 진행됩니다.</del></p>
<h2 id="문제">문제</h2>
<p><a href="https://www.acmicpc.net/problem/2776">백준2776 - 암기왕</a>
<img alt="" src="https://velog.velcdn.com/images/edocnuyh/post/7b64f5be-b7d0-4af2-a340-6c373eea5c25/image.png" /></p>
<h2 id="의문">의문</h2>
<h3 id="1-테스트케이스-t-어디에-쓰는거지">1. 테스트케이스 T? 어디에 쓰는거지</h3>
<p>일단 문제에서 하라는 대로, 입력을 받는 코드부터 쓰기 시작했다. </p>
<pre><code class="language-java">    // 1트 코드
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt(); // 쓰이는 곳 없는 외로운 int...
        int N = sc.nextInt();
        List&lt;Integer&gt; note1 = new ArrayList&lt;&gt;();
        for (int i = 0; i &lt; N; i++) {
            note1.add(sc.nextInt());
        }

        int M = sc.nextInt();
        int[] note2 = new int[M];
        for (int i = 0; i &lt; M; i++) {
            note2[i] = sc.nextInt();
        }

        for (int i = 0; i &lt; note2.length; i++) {
            int res = note1.indexOf(note2[i]) &gt; -1 ? 1 : 0;
            System.out.println(res);
        }
    }</code></pre>
<p>근데 장렬하게 떠오른 <strong>틀렸습니다!</strong> ㅜㅜ
<img alt="" src="https://velog.velcdn.com/images/edocnuyh/post/6285715b-762c-472d-ba36-c2147e9db0e9/image.png" /></p>
<p>마음이 아파요.. 왜 틀렸는지 말이라도 해주면 안돼? 
안되는구나.. </p>
<p>일단 다시 찬찬히 내 코드를 살펴보았다. 그리고 입력은 받았지만 전혀 쓰이지 않는 <code>int T</code> 요놈을 발견했다. </p>
<p>근데.. 아무리 질문을 읽어봐도 T 머 어쩌라는겨? 이 생각만 들었다. 입출력 예제도 테스트케이스가 1인 건만 있어서.. 질문을 이해를 못함. </p>
<p>그냥 대강 <code>테스트케이스 = 연종이 따라다닌 날짜</code> 이렇게 이해하기로 함. &gt;&gt; 테스트 케이스(T)만큼 질답 반복 필요.</p>
<br />


<h3 id="2-뭘-묻고-싶은-걸까">2. 뭘 묻고 싶은 걸까?</h3>
<p>코테 배경지식(자료구조, 알고리즘 등)이 머릿속에 정립되지 않은 나.. 문제만 읽었을 때 이 친구의 의중을 파악해야하는데. 아직은 그게 어려운 것 같다. 그래도 백준 사이트에서는 나름의 힌트가 적혀있었다.
<img alt="" src="https://velog.velcdn.com/images/edocnuyh/post/16aa7dee-2249-42c2-8af7-b7e5dfb818c0/image.png" /></p>
<p>응.. 정렬,, 이분 탐색.. 이런거 관련이구나. 여기서 정리를 하고 넘어가야겠지(하기싫다..)</p>
<h4 id="기존에-알던-것">기존에 알던 것</h4>
<p>일단 <code>이진 탐색(이분 탐색)</code>이라는 것에 대해 대강 알고 있던 바는 데이터를 <code>정렬</code>하고, 이걸 반띵(이분)하면서 탐색하는 것임.
정렬을 한다 &gt; 순서가 생김
반띵탐색 &gt; 대소비교가 가능함, 탐색의 범위를 점차 좁혀나갈 수 있음.</p>
<br />

<h4 id="새롭게-알게된-것">새롭게 알게된 것</h4>
<h5 id="1-이진탐색">1. 이진탐색</h5>
<p><a href="https://velog.io/@kwontae1313/%EC%9D%B4%EC%A7%84-%ED%83%90%EC%83%89Binary-Search-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B0%9C%EB%85%90">참고블로그1 - 이진탐색</a></p>
<ul>
<li>탐색 범위를 반으로 나누어 찾는 값을 포함하는 범위를 좁혀가는 방식으로 동작. 주로 배열의 인덱스를 기준으로 배열 내의 값을 탐색하는데 사용되나 리스트, 트리 등에서도 사용가능.</li>
<li>그러나 정렬된 구조에서 사용가능하므로 <strong>정렬된</strong> 리스트나 트리에서 사용이 가능하다.  </li>
</ul>
<br />

<h5 id="2-treeset">2. TreeSet</h5>
<p><a href="https://sgcomputer.tistory.com/104">참고블로그2 - TreeSet</a></p>
<ul>
<li>Set의 인터페이스를 구현한 컬렉션 클래스. &gt; Set은 중복제거~</li>
<li>이진탐색트리 자료구조 형태로 데이터를 저장한다. (자동정렬해줌)</li>
</ul>
<br />

<h5 id="3-적용">3. 적용</h5>
<p>'수첩1'에서 자료를 빠르게 찾아야 하는거니까, 수첩1의 자료형으로 TreeSet을 써보기로 함!</p>
<h2 id="고난">고난</h2>
<h3 id="계속되는-시간초과">계속되는 시간초과</h3>
<p>근데 자꾸 시간초과가 나.. 아무래도 빠르게 못찾는거지.. 
<img alt="살려주세요" src="https://velog.velcdn.com/images/edocnuyh/post/84782d28-64f7-4ccf-88ff-059ca80790db/image.png" /></p>
<p>일단 이때 코드는 이런상태였다.</p>
<pre><code class="language-java">    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); // Scanner 사용
        int T = sc.nextInt();

        for (int j = 0; j &lt; T; j++) {
            int N = sc.nextInt();
            Set&lt;Integer&gt; note1 = new TreeSet&lt;&gt;(); // TreeSet 사용
            for (int i = 0; i &lt; N; i++) {
                note1.add(sc.nextInt());
            }

            int M = sc.nextInt();
            int[] note2 = new int[M];
            for (int i = 0; i &lt; M; i++) {
                note2[i] = sc.nextInt();
            }

            for (int i = 0; i &lt; note2.length; i++) {
                int res = note1.contains(note2[i]) ? 1 : 0;
                System.out.println(res); // System.out.println으로 반복 출력
            }
        }
    }</code></pre>
<p>자꾸 시간초과가 나니까 TreeSet을 쓰는게 답이 아닌가? 생각했는데 원인은 다른데 있었다.</p>
<p><strong><code>Scanner/System.out</code></strong></p>
<p>System 함수들을 BufferedReader, StringBuilder로 전환하고 나니 시간초과 하지 않고 채점을 통과했다. </p>
<br />

<h3 id="최종제출코드">최종제출코드</h3>
<p>아래는 최종 제출 코드이다.</p>
<pre><code class="language-java">    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int j = 0; j &lt; T; j++) {
            int N = Integer.parseInt(br.readLine());
            Set&lt;Integer&gt; note1 = new TreeSet&lt;&gt;();
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i &lt; N; i++) {
                note1.add(Integer.parseInt(st.nextToken()));
            }

            int M = Integer.parseInt(br.readLine());
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i &lt; M; i++) {
                int res = note1.contains(Integer.parseInt(st.nextToken())) ? 1 : 0;
                System.out.println(res);
            }
        }
    }</code></pre>
<h2 id="정리">정리</h2>
<ul>
<li><strong>TreeSet</strong>: 이진탐색트리 자료구조 형태로 데이터를 중복없이 저장</li>
<li><strong>이진탐색</strong>: <code>정렬</code>이 주요 포인트!</li>
<li>시간이 중요하다면 입출력은 System 함수말고 BufferedReader, StringBuilder 사용하자.</li>
</ul>