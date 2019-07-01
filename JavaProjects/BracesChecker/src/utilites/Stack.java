package utilites;

public class Stack<T> implements AbstractStack<T>{
    private class Node{
        Object data;
        Node next;

        Node(T dat){
            data = dat;
        }
    }

    private Node top = null;
    private int size = 0;

    public Stack(){}

    @Override
    public void push(T dat){
        Node node = new Node(dat);
        node.next = top;
        top = node;
        size++;
    }

    @Override
    public T pop(){
        if(!isEmpty()) {
            T res = (T) top.data;
            top = top.next;
            size--;
            return res;
        } else {
            throw new IndexOutOfBoundsException("Stack is empty");
        }
    }

    @Override
    public T top(){
        if(!isEmpty()) {
            return (T) top.data;
        } else {
            throw new IndexOutOfBoundsException("Stack is empty");
        }
    }

    @Override
    public boolean isEmpty(){
        return size == 0;
    }

    @Override
    public int size(){
        return size;
    }
}
