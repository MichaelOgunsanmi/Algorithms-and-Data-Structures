package com.dataStructuresArrays;

public class Array {
    private int [] items;
    private int count;

    public Array(int length) {
        this.items = new int [length];
    }

    public void insert(int item){
        if (this.items.length == this.count && this.count != 0){
            int [] newItems = new int[this.count * 2];

            for (int i = 0; i < this.count; i++)
                newItems[i]= this.items[i];

            this.items = newItems;
        }

        this.items[count++] = item;
    }

    public void remove(int index){
        if (index < 0 || index >= this.count)
            throw new IllegalArgumentException();

        for (int i = index; i < this.count; i++)
            this.items[i] = this.items[i+1];

        count--;
    }

     public int indexOf(int item){
         for (int i = 0; i < this.count; i++)
             if (this.items[i] == item)
                 return i;

         return -1;
     }

     public int max(){
        var max = Integer.MIN_VALUE;

         for (int i = 0; i < this.count; i++)
             if (this.items[i] > max)
                 max = this.items[i];

         return max;
     }

     public int[] intersect(Array compareArray){
        var intersect = new Array(0);
        var compareLength = compareArray.count;
        var smaller = Math.min(this.count, compareLength);

         for (int i = 0; i < smaller; i++)
             if (smaller == this.count && compareArray.indexOf(this.items[i]) != -1 )
                intersect.insert(this.items[i]);
             else if(indexOf(compareArray.items[i]) != -1)
                 intersect.insert(compareArray.items[i]);
         return intersect.items;
     }

     public Array reverse(){
         var forwardIndex = 0;
         var backwardIndex = this.count - 1;

         while (forwardIndex < backwardIndex){
             var temp = this.items[forwardIndex];

             this.items[forwardIndex] = this.items[backwardIndex];
             this.items[backwardIndex] = temp;

             forwardIndex++;
             backwardIndex--;
         }

         return this;
     }

     public Array insertAt(int item, int index){
        if (this.items.length == this.count && this.count != 0){
             int [] newItems = new int[this.count * 2];

             for (int i = 0; i < this.count; i++)
                 newItems[i]= this.items[i];

             this.items = newItems;
         }
        if (index > this.count)
            throw new IllegalArgumentException();

        while(index <= this.count){
            var temp = this.items[index];

            this.items[index] = item;

            index++;
            item = temp;
        }

         count++;
         System.out.println(this.count);
        return this;
     }

    public void print(){
        for (int i = 0; i < this.count; i++)
            System.out.println(this.items[i]);
    }
}
