package utilites;

interface AbstractStack<T>{
    void push(T data);
    T pop();
    T top();
    boolean isEmpty();
    int size();
}
