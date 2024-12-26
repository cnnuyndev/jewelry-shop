from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Address(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    locality = models.CharField(max_length=150, verbose_name="số nhà, thôn, xã, phường, huyện: ")
    city = models.CharField(max_length=150, verbose_name="Tỉnh, Thành phố: ")
    state = models.CharField(max_length=150, verbose_name="Số điện thoại: ")

    def __str__(self):
        return self.locality
    class Meta:
        verbose_name =("Quản lý Địa chỉ")
        verbose_name_plural =("Quản lý Địa chỉ")

class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name="Tên Danh mục")
    slug = models.SlugField(max_length=55, verbose_name="Category Slug")
    description = models.TextField(blank=True, verbose_name="Mô tả")
    category_image = models.ImageField(upload_to='category', blank=True, null=True, verbose_name="Image Danh mục: ")
    is_active = models.BooleanField(verbose_name="Active")
    is_featured = models.BooleanField(verbose_name="Nổi bật")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Date")

    class Meta:
        verbose_name_plural = 'Quản lý Danh mục'
        ordering = ('-created_at', )

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name="Tên sản phẩm")
    slug = models.SlugField(max_length=160, verbose_name="Product Slug")
    sku = models.CharField(max_length=255, unique=True, verbose_name="Mã sản phẩm")
    short_description = models.TextField(verbose_name="Mô tả")
    detail_description = models.TextField(blank=True, null=True, verbose_name="Mô tả chi tiết")
    product_image = models.ImageField(upload_to='product', blank=True, null=True, verbose_name="Image sản phẩm")
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, verbose_name="Phân loại sản phẩm", on_delete=models.CASCADE)
    is_active = models.BooleanField(verbose_name="Active")
    is_featured = models.BooleanField(verbose_name="Nổi bật")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Date")

    class Meta:
        verbose_name_plural = 'Quản lý Sản phẩm'
        ordering = ('-created_at', )

    def __str__(self):
        return self.title


class Cart(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name="Sản phẩm", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, verbose_name="Số lượng")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Date")
    class Meta:
        verbose_name =("Quản lý Giỏ hàng")
        verbose_name_plural =("Quản lý Giỏ hàng")
    def __str__(self):
        return str(self.user)
    
    # Creating Model Property to calculate Quantity x Price
    @property
    def total_price(self):
        return self.quantity * self.product.price

class Like(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name="Sản phẩm", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Date")
    class Meta:
        verbose_name_plural =("Quản lý sản phẩm yêu thích")
        ordering = ('-created_at', )

    def __str__(self):
        return str(self.product)
STATUS_CHOICES = (
    # ('Pending', 'Pending'),
    # ('Accepted', 'Accepted'),
    # ('Packed', 'Packed'),
    # ('On The Way', 'On The Way'),
    # ('Delivered', 'Delivered'),
    # ('Cancelled', 'Đã hủy')
    ('Chờ xác nhận', 'Chờ xác nhận'),
    ('Chờ lấy hàng', 'Chờ lấy hàng'),
    ('Đang giao', 'Đang giao'),
    ('Đã giao', 'Đã giao'),
    ('Trả hàng', 'Trả hàng'),
    ('Đã hủy', 'Đã hủy')
)


class Order(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    address = models.ForeignKey(Address, verbose_name="Địa chỉ giao hàng", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name="Sản phẩm", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name="Số lượng")
    ordered_date = models.DateTimeField(auto_now_add=True, verbose_name="Ngày đặt hàng")
    status = models.CharField(
        verbose_name="Trạng thái",
        choices=STATUS_CHOICES,
        max_length=50,
        default="Chờ xác nhận"
        )
    class Meta:
        verbose_name =("Quản lý Đơn hàng")
        verbose_name_plural =("Quản lý Đơn hàng")
    def __str__(self):
        return str(self.user)
class Blog(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    title = models.CharField(max_length=150, verbose_name="Tên bài viết")
    slug = models.SlugField(max_length=160, verbose_name="blog Slug")
    short_description = models.TextField(verbose_name="Mô tả")
    detail_description = models.TextField(blank=True, null=True, verbose_name="Mô tả chi tiết")
    blog_image = models.ImageField(upload_to='product', blank=True, null=True, verbose_name="Image sản phẩm")
    is_featured = models.BooleanField(verbose_name="Nổi bật")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Date")
    class Meta:
        verbose_name =("Quản lý Bài viết")
        verbose_name_plural =("Quản lý Bài viết")
    def __str__(self):
        return str(self.title)