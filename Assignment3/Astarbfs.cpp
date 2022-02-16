#include<bits/stdc++.h>
using namespace std;


map<char , int> mp;
map<char , int> :: iterator it;
char ch[10000];

#define MX 1005
#define INF 1000000000
typedef pair<int, int> pi;

struct node{
    int val;
    int cost;
};

struct node1{
   int hu;
};


vector<node1> hueri[MX];
vector<node> G[MX];

bool vis[MX];
int dis[MX];
int parent[MX];

int nodes,edges;
int src;

void clear_(){
    for (int i = 0; i < MX; i++){
        G[i].clear();
    }
}

void gbfs(char src , char tar , int n){

    vector<bool> visited(n, false);
    priority_queue<pi, vector<pi>, greater<pi> > open;

    vector<pair<int,int>> closed;

    open.push(make_pair(hueri[mp[src]][0].hu+ G[mp[src]][0].cost , mp[src]));
    int s = mp[src];
    visited[s] = true;

    while(!open.empty()){

        int val = open.top().second;
        open.pop();

        closed.push_back(make_pair(val , parent[val]));

        if (val == mp[tar])
            break;

        for(int i = 0; i < G[val].size(); i++){
            if (!visited[G[val][i].val]) {
                int nxt_node =  G[val][i].val;
                visited[G[val][i].val] = true;
                parent[nxt_node] = val;
                open.push(make_pair(hueri[nxt_node][0].hu +G[val][i].cost ,G[val][i].val));
            }

        }

    }



   for(int i = 0 ; i<closed.size() ; ++i){
        char ch1 = ch[closed[i].first];
        char ch2 = ch[closed[i].second];
     cout<<ch1 <<" "<<ch2<<endl;
   }
}

int main(){

    clear_();

    cin>>nodes>>edges;


    for(int i = 1 ; i<=nodes ; ++i){
        cin >> ch[i];
        mp[ch[i]] = i;
    }

    for(int i=1;i<=edges;i++){

        char u, v , edgecost;
        cin >> u >> v >> edgecost;
        G[mp[u]].push_back({mp[v] , edgecost});
    }


    for(int i = 1 ; i<=nodes; ++i){

        char ch ; int h;
        cin >> ch >> h;

        hueri[mp[ch]].push_back({h});
    }

    gbfs('S' , 'E' , 13);


  return 0;
}
/*
5 9
1 2
1 3
1 4
2 3
2 4
3 4
3 5
4 5
1 5
10 20 30 40 50


13 16
1 2
1 3
1 4
2 3
2 5
3 5
3 9
5 7
9 7
9 8
8 6
4 13
13 10
13 11
10 12
11 12
10 9 7 8 8 0 6 3 6 4 4 3 6


13 16
S
A
B
C
D
E
F
G
H
I
J
K
L
S A 7
S B 2
S C 3
A B 3
A D 4
B H 1
B D 4
D F 5
H F 3
H G 2
G E 2
C L 2
L I 4
L J 4
I K 4
J K 4
S 10
A 9
B 7
C 8
D 8
E 0
F 6
G 3
H 6
I 4
J 4
K 3
L 6
*/
