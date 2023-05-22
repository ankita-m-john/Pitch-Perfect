import torch.nn as nn
class SiameseNetwork(nn.Module):
    def __init__(self):
        super(SiameseNetwork, self).__init__()
        print("Alia5")
        self.reflection_pad = nn.ReflectionPad2d(1)
        self.conv1 = nn.Conv2d(1, 4, kernel_size=3)
        self.conv2 = nn.Conv2d(4, 8, kernel_size=3)
        self.conv3 = nn.Conv2d(8, 8, kernel_size=3) 
        self.relu = nn.ReLU(inplace=True)
        self.batch_norm1 = nn.BatchNorm2d(4)
        self.batch_norm2 = nn.BatchNorm2d(8) 
        self.fc1 = nn.Linear(8 * 100 * 100, 500)
        self.fc2 = nn.Linear(500, 500)
        self.fc3 = nn.Linear(500, 5)
        
    def forward_one_branch(self, x):
        x = self.batch_norm1(self.relu(self.conv1(self.reflection_pad(x))))
        x = self.batch_norm2(self.relu(self.conv2(self.reflection_pad(x))))        
        x = self.batch_norm2(self.relu(self.conv3(self.reflection_pad(x))))   
        x = x.view(x.size()[0], -1)
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))        
        x = self.fc3(x)
        
        return x
        
    def forward(self, input1, input2):
        output1 = self.forward_one_branch(input1)
        output2 = self.forward_one_branch(input2)     
        
        return output1, output2
# Function to search the specified array `nums` for key `target`
# using the binary search algorithm
def binarySearch(nums, target):
    low = 0
    high = len(nums) - 1
 
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            return mid      # key found
 
    return low              # key not found
 
 
# Function to find the `k` closest elements to `target` in a sorted integer array `nums`
def findKClosestElements(nums, target, k):
 
    # find the insertion point using the binary search algorithm
    i = binarySearch(nums, target)
 
    left = i - 1
    right = i
 
    # run `k` times
    while k > 0:
 
        # compare the elements on both sides of the insertion point `i`
        # to get the first `k` closest elements
 
        if left < 0 or (right < len(nums) and abs(nums[left] - target) > abs(nums[right] - target)):
            right = right + 1
        else:
            left = left - 1
 
        k = k - 1
 
    # return `k` closest elements
    return nums[left+1: right]
 
def songrec():
    import mysql.connector
    import sys
    import torch.nn as nn
    sys.path.insert(0,'D:\\Main Project\\Pitch-Perfect\\SNN model')
    from modelling import Score
    song_id = 3 #Must get from UI
    mydb = mysql.connector.connect(host = "127.0.0.1", user = "root",password = "ankita", auth_plugin='mysql_native_password', database = "Pitch_Perfect")
    cur = mydb.cursor()
    cur.execute("SELECT song_id,Total_Score FROM Scoring ORDER BY Total_Score")
    result = cur.fetchall()
    nums = []
    for x in result:
        nums.append(x[1])
    cur.execute("SELECT Total_Score FROM Scoring WHERE song_id = %s",(song_id,))
    result = cur.fetchall()
    # nums = [10, 12, 15, 17, 18, 20, 25]
    k = 1 #Change after completing db
    target = round(Score * result[0][0] / 100)
    print(target)
    L = findKClosestElements(nums, target, k)
    print(L)
    cur.execute("SELECT s.name FROM Song as s WHERE s.song_id= (SELECT song_id FROM Scoring WHERE Total_Score>= %s AND Total_Score<=%s ORDER BY Total_Score)",(L[0],L[-1]))
    out = cur.fetchall()
    for x in out:
        print(x[0])
if __name__ == '__main__':
    songrec()