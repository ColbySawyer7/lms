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
 * Base User model.
 * @export
 * @interface UserRead
 */
export interface UserRead {
    /**
     * 
     * @type {any}
     * @memberof UserRead
     */
    'id'?: any;
    /**
     * 
     * @type {string}
     * @memberof UserRead
     */
    'email': string;
    /**
     * 
     * @type {boolean}
     * @memberof UserRead
     */
    'is_active'?: boolean;
    /**
     * 
     * @type {boolean}
     * @memberof UserRead
     */
    'is_superuser'?: boolean;
    /**
     * 
     * @type {boolean}
     * @memberof UserRead
     */
    'is_verified'?: boolean;
}

