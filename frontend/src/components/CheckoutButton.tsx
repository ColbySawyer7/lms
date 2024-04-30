import React from 'react';
import { basePath } from '../providers/env';
import { notDeepEqual } from 'assert';
import { fetchUtils, useGetIdentity } from 'react-admin';
import { useNotify } from 'react-admin';


interface CheckoutBookProps {
    book: number; 
}




const BookDetail: React.FC<CheckoutBookProps> = ({ book }) => {
    const notify = useNotify();
    const user = useGetIdentity();
    const handleBookCheckout = (bookId: number) => {
        console.log(`Checking out book with ID: ${bookId}`);
        // Implement the checkout logic, possibly involving an API call
    };

    const handleCheckout = async () => {
        try{
            const url = `${basePath}/api/v1/transactions`;
            const options= {
                method: 'POST',
                body: JSON.stringify({book_id: book, user_id: user.identity?.id, library_id: 1}),
                headers: new Headers ({
                    Accept: 'application/json',
                    Authorization: `Bearer ${localStorage.getItem('token')}`
                })
            };
            await fetchUtils.fetchJson(url, options);
            notify('Book checked out successfully');
        } catch (error) {
            notify('An error occurred while checking out the book');

        }
    }

    return (
        <div>
            <button onClick={() => handleCheckout()}>Checkout</button>
        </div>
    );
};

export default BookDetail;
