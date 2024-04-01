#include<bits/stdc++.h>
using namespace std;

vector<int> mergeArrays(const vector<int>& arr1, const vector<int>& arr2) {
  int n1 = arr1.size();
  int n2 = arr2.size();

  vector<int> merged_arr(n1 + n2);

  int i = 0, j = 0, k = 0;

  while (i < n1 && j < n2) {
    if (arr1[i] < arr2[j]) {
      merged_arr[k] = arr1[i];
      i++;
    } else {
      merged_arr[k] = arr2[j];
      j++;
    }
    k++;
  }

  while (i < n1) {
    merged_arr[k] = arr1[i];
    i++;
    k++;
  }

  while (j < n2) {
    merged_arr[k] = arr2[j];
    j++;
    k++;
  }

  return merged_arr;
}

int main() {
  int n1,n2;cin>>n1>>n2;
  vector<int> arr1(n1),arr2(n2);
  for(int i =0;i<n1;i++){
    cin>>arr1[i];
  }
  for(int i =0;i<n2;i++){
    cin>>arr2[i];
  }
  vector<int> merged_arr = mergeArrays(arr1, arr2);
  
  for (int num : merged_arr) {
    cout << num << " ";
  }
  cout << endl;

  return 0;
}
