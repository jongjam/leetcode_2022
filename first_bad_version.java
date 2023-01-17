public class first_bad_version {
    /* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */
    

    public int firstBadVersion(int n) {
        // binary search this bitch?

        //Attempt one, start at the one half
        //If the half mark is good, go backwards
        //If it's not, go up by half again ?

        //son of a bitch it is binary search
        int start = 0;
        int end = n;

        //if start is good and end is bad then we know it is in between the two of them
        //if mid is bad then we know that 
        while (start < end) {
            int mid = start + (end - start) / 2;
            if (isBadVersion(mid)) { //if it's bad.... then I know I can go down
                end = mid; //start counting back???
            } else { //if its good then I need to move up
                start = mid + 1;
            } //when do i know to stop the binary searh
        } 


        return start; //for some reason... this just works.... why tho?
    }

    //skip ahead and find where it's bad
    //and then roll backwards? 
    //isBadVersion();
}
