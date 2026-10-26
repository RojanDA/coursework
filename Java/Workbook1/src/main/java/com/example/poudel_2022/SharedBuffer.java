package com.example.poudel_1002238306;

import java.util.LinkedList;
import java.util.Queue;
import java.util.concurrent.locks.ReentrantLock;

public class SharedBuffer {
    private final Queue<String> buffer;
    private final ReentrantLock lock;
    private volatile boolean productionComplete;

    public SharedBuffer() {
        this.buffer = new LinkedList<>();
        this.lock = new ReentrantLock();
        this.productionComplete = false;
    }

    public void add(String item) {
        lock.lock();
        try {
            buffer.add(item);
        } finally {
            lock.unlock();
        }
    }

    public String remove() {
        lock.lock();
        try {
            if (buffer.isEmpty()) {
                return null;
            }
            return buffer.remove();
        } finally {
            lock.unlock();
        }
    }

    public boolean isEmpty() {
        lock.lock();
        try {
            return buffer.isEmpty();
        } finally {
            lock.unlock();
        }
    }

    public void setProductionComplete() {
        productionComplete = true;
    }

    public boolean isProductionComplete() {
        return productionComplete && isEmpty();
    }

    public int size() {
        lock.lock();
        try {
            return buffer.size();
        } finally {
            lock.unlock();
        }
    }
}