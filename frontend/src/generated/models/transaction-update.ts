/* tslint:disable */
/* eslint-disable */
/**
 * lms
 * lms API
 *
 * The version of the OpenAPI document: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */



/**
 * 
 * @export
 * @interface TransactionUpdate
 */
export interface TransactionUpdate {
    /**
     * 
     * @type {number}
     * @memberof TransactionUpdate
     */
    'book_id': number;
    /**
     * 
     * @type {string}
     * @memberof TransactionUpdate
     */
    'user_id': string;
    /**
     * 
     * @type {number}
     * @memberof TransactionUpdate
     */
    'library_id': number;
    /**
     * 
     * @type {string}
     * @memberof TransactionUpdate
     */
    'status': string;
    /**
     * 
     * @type {string}
     * @memberof TransactionUpdate
     */
    'return_date': string;
}

